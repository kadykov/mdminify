# src/my_markdown_tool/cli.py
import click
from .mdminify import process_markdown_file, restore_links_from_json


@click.group()
def cli():
    """CLI tool to remove and restore markdown links."""
    pass


@click.command()
@click.argument("input_md_file", type=click.Path(exists=True))
@click.argument("output_md_file", type=click.Path())
@click.argument("output_json_file", type=click.Path())
def remove(input_md_file, output_md_file, output_json_file):
    """Remove links from a markdown file and save the links to a JSON file."""
    process_markdown_file(input_md_file, output_md_file, output_json_file)
    click.echo(
        f"Processed markdown saved to {output_md_file}, links saved to {output_json_file}"
    )


@click.command()
@click.argument("plain_md_file", type=click.Path(exists=True))
@click.argument("json_file", type=click.Path(exists=True))
@click.argument("output_md_file", type=click.Path())
def restore(plain_md_file, json_file, output_md_file):
    """Restore links from a JSON file into a markdown file."""
    restore_links_from_json(plain_md_file, json_file, output_md_file)
    click.echo(f"Restored markdown with links saved to {output_md_file}")


# Add the commands to the CLI group
cli.add_command(remove)
cli.add_command(restore)

if __name__ == "__main__":
    cli()
