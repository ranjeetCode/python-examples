# Highest to lower precedence
# 1. ()
# 2. ** Exponentiation
# 3. %, /, //, *
# 4. +, -

# Expression: (9-7)*2**3+10%6//-1*2-1
#Solution:
#                   (9-7)
        # Step1: 2*2**3+10%6//-1*2-1
#                  2**3
        # Step2: 2*8+10%6//-1*2-1
#                 2*8 + 10%6 // -1 *2 -1
        # Step3: 16 + -8 -1

        #Step4: 7

exp1 = (9-7)*2**3+10%6//-1*2-1
print (exp1)

# In the below expression 3 and 4 are added first since they are in parentheses,
# resulting in the expression 15 / 3 * 2 * 2 - 7.
# Since division and multiplication have the same level of priority, they are done from left to right,
# with 15 divided by 3 becoming 5, 5 times 2 becoming 10, and 10 times 2 becoming 20. Finally, 7 is subtracted from 20,
# resulting in 13.

exp2 = 15 / 3 * 2 * 2 - (3 + 4)
print(exp2)