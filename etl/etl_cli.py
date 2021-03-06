import click

from etl.run_etl import run_etl
from etl import __version__


@click.command()
# @click.option('--log-level',
#               type=click.Choice(['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']),
#               required=False, default=None, help='Python logging level (for the console).')
@click.option('--container', type=str,
              required=False, help='Name of Azure container to download the data from.')
@click.option('--blob', type=str,
              required=False, help='Name of Azure blob storage.')
@click.option('--media', type=str,
              required=False, help='Name of media to download the data from.')
@click.option('--temp-dir', type=click.Path(file_okay=False, dir_okay=True, exists=True), default='/tmp',
              required=False, help='Path to data directory to download the data.')
@click.option('--data-dir', type=click.Path(file_okay=False, dir_okay=True, exists=True), default=None,
              required=False, help='Path to data directory to download the data. '
                                   'If given, data should be in local storage. '
                                   '(No download from Azure) ')
@click.option('--data-source', type=click.Choice(['local', 'azure']), default='azure',
              required=False, help='Source of data.')
@click.option('--target-storage', type=click.Choice(['local', 'postgre']), default='postgre',
              required=False, help='Target to store the ETL output.'
                                   ' If "local", will save in csv, '
                                   ' if "postgre", will insert each trash in Postgre database. ')
@click.option('--ai-url', type=str,
              required=False, help='URL of AI. If not given, will be set from ENV.')
def cli(container, blob, media, temp_dir, data_dir, data_source, ai_url, target_storage):
    """Run the ETL

    Use command `python etl_cli.py --help` to get a list of the options .
    """

    # Run the etl flow
    run_etl(
        container_name=container,
        blob_name=blob,
        media_name=media,
        temp_dir=temp_dir,
        data_dir=data_dir,
        data_source=data_source,
        target_storage=target_storage,
        ai_url=ai_url
    )


@click.command()
def version():
    """Print version and exit"""
    click.echo(f'ETL version {__version__}.')


if __name__ == '__main__':
    cli()
