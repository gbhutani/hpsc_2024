program mult 
implicit none
integer, parameter :: n=100
real (kind=8), dimension(n,n) :: A,B,C
integer :: i,j,k

A=1.d0
B=2.d0

! Matrix multiplication: C = A * B 
!$acc parallel loop collapse(2) present(A,B,C) 
do i = 1, n 
        do j = 1, n 
                C(i,j) = 0.0 
                do k = 1, n 
                        C(i,j) = C(i,j) + A(i,k) * B(k,j) 
                end do 
        end do 
end do 
!$acc end parallel loop

print*, C
end program mult
