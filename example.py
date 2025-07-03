import marimo

__generated_with = "0.14.9"
app = marimo.App(width="medium")


@app.cell
def _():
    examples = [
        {"text": """# Заголовок первого уровня

    Это обычный текст.

    ## Заголовок второго уровня

    Здесь можно добавить **жирный текст**, *курсив* или `встроенный код`.

    ### Заголовок третьего уровня

    Вот список:
    *   Элемент списка 1
    *   Элемент списка 2
        *   Подэлемент списка

    Вот цитата:
    > Это цитата.

    Вот ссылка: [пример ссылки](https://www.example.com)

    Вот таблица:

    | Заголовок 1 | Заголовок 2 |
    |---|---|
    | Значение 1 | Значение 2 |"""},
        {"text": """# Заголовок первого уровня

    Это обычный текст.

    ## Заголовок второго уровня

    Здесь можно добавить **жирный текст**, *курсив* или `встроенный код`.

    ### Заголовок третьего уровня

    Вот список:
    *   Элемент списка 1
    *   Элемент списка 2
        *   Подэлемент списка

    Вот цитата:
    > Это цитата.

    Вот ссылка: [пример ссылки](https://www.example.com)

    Вот таблица:

    | Заголовок 1 | Заголовок 2 |
    |---|---|
    | Значение 1 | Значение 2 |"""}
    ]
    return (examples,)


@app.cell
def _(examples):
    import markdown
    from markdown.extensions.tables import TableExtension

    from molabel import SimpleLabel

    def render_example(example):
        html = markdown.markdown(
            example['text'],
            extensions=[TableExtension()]
        )
        return html

    # Create annotation widget
    widget = SimpleLabel(
        examples=examples,
        render=render_example,
        notes=True
    )

    # Display in notebook
    widget
    return (widget,)


@app.cell
def _(widget):
    annotations = widget.get_annotations()
    annotations
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
