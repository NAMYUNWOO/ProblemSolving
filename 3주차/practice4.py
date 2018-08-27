import elice_utils

def merge(tmp, size):
    # merge two sierpinksi triangles
    res = ''
    for idx, elem in enumerate(tmp.split('\n')):
        res += elem +' '*(2**(size-1)-idx) + elem + '\n'
    return res.rstrip('\n')


def draw_triangle(size):
    # Implement here 
    # 시어핀스키 삼각형을 리턴하세요. Δ를 사용하여 삼각형 하나를 표현하시면 됩니다. 
    tri = 'Δ'
    if size == 1:
        return tri
    else:
        tmp = draw_triangle(size-1)
        top = ' '*2**(size-2) + tmp 
        top = top.replace('\n', '\n'+' '*2**(size-2))
        bot = merge(tmp, size-1)
        
        return top + '\n' + bot

def main():
    size = int(input())
    print(draw_triangle(size))

if __name__ == "__main__":
    main()
