from tasks.draw_tree import draw_tree


def test_draw_tree():

    radius: int = 5

    assert_tree: str = (
        '    *    \n'
        '   ***   \n'
        '  *****  \n'
        ' ******* \n'
        '*********\n'
        '    |    \n'
    )

    assert draw_tree(radius) == assert_tree
