from IEEE754 import IEEE754

if __name__ == "__main.py__":
    my_num = 13.375
    ieee754 = IEEE754(my_num)
    
    print("Integer part: ", ieee754.integer_part)
    print("Decimal part: ", ieee754.decimal_part)
    print("Exponent part: ", ieee754.exponent_part)

    