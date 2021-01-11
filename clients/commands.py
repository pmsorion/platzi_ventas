import click

@click.group()
def clients():
    """Manages the clients lifeclycle"""
    pass


@clients.command()
@click.pass_context
def create(ctx, name, company, email, position):
    """Creates a new cliente"""


@clients.command()
@click.pass_context
def list(ctx):
    """List all clientes"""
    pass


@clients.command()
@click.pass_context
def update(ctx, client_uid):
    """Updates a clients"""
    pass


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """Delete a client"""
    pass


all = clients
