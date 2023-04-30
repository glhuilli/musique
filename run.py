import click

from musique.utils.openai import ask_chatgpt


def check_prompt(prompt: str) -> bool:
    words = prompt.split()
    if len(words) >= 2:
        return True
    else:
        click.echo("Please enter at least 2 words.")
    return False


@click.command()
@click.option('--prompt', prompt='Please enter the type of list you want to generate',
              help='Input prompt to generate list.')
def main(prompt: str) -> None:
    """
    Call ChatGPT but only if prompt is reasonable (review check_prompt for current implementation)
    """
    if check_prompt(prompt):
        response = ask_chatgpt(prompt)
        for song in response:
            print(song)


if __name__ == '__main__':
    main()
