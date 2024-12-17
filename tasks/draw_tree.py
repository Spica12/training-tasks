
def draw_tree(radius: int = 3) -> str:
    '''
    example: draw_tree(5)

        *
       ***
      *****
     *******
    *********
        |
    '''
    tree: str = ''
    symbol: str = '*'
    row: str = symbol

    diametr: int = radius * 2 - 1
    height: int = radius + 1

    for i in range(1, height):
        if i > 1:
            row: str = row + 2 * symbol

        formated_row: str = f"{row:^{diametr}}\n"
        tree += formated_row

    tree += f"{'|':^{diametr}}\n"


    return tree


def main():
    tree: str = draw_tree(5)
    print(tree)


if __name__ == '__main__':
    main()
