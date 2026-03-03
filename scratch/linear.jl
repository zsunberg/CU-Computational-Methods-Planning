import LinearAlgebra
using BenchmarkTools

function det(m::AbstractMatrix)
    nr, nc = size(m)
    if nr == 1
        return only(m)
    end
    detval = zero(eltype(m))
    for c in 1:nc
        sign = isodd(c) ? one(eltype(m)) : -one(eltype(m))
        detval += sign * m[1, c] * det(m[2:nr, [1:c-1; c+1:nc]])
    end
    return detval
end

m = [1 2; 3 4]

# @enter det(m)

@show det(m)
@show LinearAlgebra.det(m)

#=
for i in 1:10
    global m = rand(10, 10)
    @assert det(m) ≈ LinearAlgebra.det(m)
end
=#

using StaticArrays

function fastdet(m::AbstractMatrix, cbits=@SVector(fill(true, size(m, 2))))
    nr = sum(cbits)
    if nr == 1
        return m[end, findfirst(cbits)]
    end
    mr = length(cbits) + 1 - nr
    detval = zero(eltype(m))
    sign = one(eltype(m))
    for mc in 1:length(cbits)
        if cbits[mc]
            sign *= -1 
            detval += sign * m[mr, mc] * fastdet(m, setindex(cbits, false, mc))
        end
    end
    return detval
end

m = rand(5, 5)
@btime LinearAlgebra.det($m)
@btime det($m)
@btime fastdet($m)

for i in 1:10
    global m = rand(5, 5)
    @assert fastdet(m) ≈ LinearAlgebra.det(m)
end
