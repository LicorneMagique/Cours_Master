.section .text
.globl main
main:
	addi	sp,sp,-16
	sd	ra,8(sp)
## Your assembly code there
	lui	a5,%hi(.LC1)
	addi	a0,a5,%lo(.LC1)
	call	print_string
	li	a0,42
	call	print_int
	call	newline
	li	a0,97
	call	print_char
	li	a0,10 #new line char
	call	print_char
	
## /end of user assembly code
	ld	ra,8(sp)
	addi	sp,sp,16
	jr	ra
	ret

# Data comes here
	.section	.data
	.align	3
.LC1:
	.string	"HI MIF08!"
