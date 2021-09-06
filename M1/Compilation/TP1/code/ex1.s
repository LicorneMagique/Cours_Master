	.file	"ex1.c"
	.option nopic
	.attribute arch, "rv64i2p0_m2p0_a2p0_f2p0_d2p0_c2p0"
	.attribute unaligned_access, 0
	.attribute stack_align, 16
# GNU C17 (GCC) version 10.2.0 (riscv64-unknown-elf)
#	compiled by GNU C version 9.3.0, GMP version 6.2.0, MPFR version 4.0.2, MPC version 1.1.0, isl version none
# GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
# options passed:  ex1.c -mtune=rocket -march=rv64imafdc -mabi=lp64d
# -march=rv64imafdc -auxbase-strip ex1.s -fverbose-asm
# options enabled:  -faggressive-loop-optimizations -fallocation-dce
# -fauto-inc-dec -fdelete-null-pointer-checks -fdwarf2-cfi-asm
# -fearly-inlining -feliminate-unused-debug-symbols
# -feliminate-unused-debug-types -ffp-int-builtin-inexact -ffunction-cse
# -fgcse-lm -fgnu-unique -fident -finline-atomics -fipa-stack-alignment
# -fira-hoist-pressure -fira-share-save-slots -fira-share-spill-slots
# -fivopts -fkeep-static-consts -fleading-underscore -flifetime-dse
# -fmath-errno -fmerge-debug-strings -fpeephole -fplt
# -fprefetch-loop-arrays -freg-struct-return
# -fsched-critical-path-heuristic -fsched-dep-count-heuristic
# -fsched-group-heuristic -fsched-interblock -fsched-last-insn-heuristic
# -fsched-rank-heuristic -fsched-spec -fsched-spec-insn-heuristic
# -fsched-stalled-insns-dep -fschedule-fusion -fsemantic-interposition
# -fshow-column -fshrink-wrap-separate -fsigned-zeros
# -fsplit-ivs-in-unroller -fssa-backprop -fstdarg-opt
# -fstrict-volatile-bitfields -fsync-libcalls -ftrapping-math -ftree-cselim
# -ftree-forwprop -ftree-loop-if-convert -ftree-loop-im -ftree-loop-ivcanon
# -ftree-loop-optimize -ftree-parallelize-loops= -ftree-phiprop
# -ftree-reassoc -ftree-scev-cprop -funit-at-a-time -fverbose-asm
# -fzero-initialized-in-bss -mdiv -mexplicit-relocs -mfdiv -mplt
# -mriscv-attribute -mstrict-align

	.text
	.section	.rodata
	.align	3
.LC0:
	.string	"%d\n"
	.text
	.align	1
	.globl	main
	.type	main, @function
main:
	addi	sp,sp,-32	#,,
	sd	ra,24(sp)	#,
	sd	s0,16(sp)	#,
	addi	s0,sp,32	#,,
# ex1.c:7:   int x = 41;
	li	a5,41		# tmp74,
	sw	a5,-20(s0)	# tmp74, x
# ex1.c:8:   x = x+1;
	lw	a5,-20(s0)		# tmp76, x
	addiw	a5,a5,1	#, tmp75, tmp76
	sw	a5,-20(s0)	# tmp75, x
# ex1.c:9:   printf("%d\n",x);
	lw	a5,-20(s0)		# tmp77, x
	mv	a1,a5	#, tmp77
	lui	a5,%hi(.LC0)	# tmp78,
	addi	a0,a5,%lo(.LC0)	#, tmp78,
	call	printf		#
# ex1.c:11:   return 0;
	li	a5,0		# _5,
# ex1.c:12: }
	mv	a0,a5	#, <retval>
	ld	ra,24(sp)		#,
	ld	s0,16(sp)		#,
	addi	sp,sp,32	#,,
	jr	ra		#
	.size	main, .-main
	.ident	"GCC: (GNU) 10.2.0"
