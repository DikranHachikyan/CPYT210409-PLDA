

if __name__ == '__main__':
    
    x = int(input('X='))
    m = 0

    # (cond)? true_expr:false_expr;
    
    m = x ** 2 if x > 0 else -x
    
    print(f'm = {m}')

    print('--- ---')    