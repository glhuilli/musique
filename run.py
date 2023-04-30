import click

from musique.utils.openai import ask_chatgpt
from musique.utils.spotify import create_playlist


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
@click.option('--playlist_name', prompt='Please enter the name of the playlist', help='Name of playlist')
def main(prompt: str, playlist_name: str) -> None:
    """
    Call ChatGPT but only if prompt is reasonable (review check_prompt for current implementation)

    Also, only calls the playlist creation step if there are songs
    """
    if check_prompt(prompt):
        songs = list(ask_chatgpt(prompt))
        if songs:
            added_songs = create_playlist(playlist_name, songs)
            print(f'Added a total of {added_songs} to the "{playlist_name}" playlist')


if __name__ == '__main__':
    main()
