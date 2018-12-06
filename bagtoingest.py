import click


@click.command()
@click.argument("path", type=click.Path(exists=True))
@click.option(
    "--checksum",
    default="md5",
    help="Type of manifest file to look for. Defaults to md5.",
)
@click.option(
    "--destination",
    default="./",
    type=click.Path(exists=True),
    help="Location of output file; include trailing /. Defaults to current directory.",
)
def cli(path, checksum, destination):
    """
    Contruct Scholar@UC import template from BagIt manifest file
    """
    with open(path + "manifest-%s.txt" % (checksum), "r") as manifest:
        with open(_outfile_name(destination), "w") as outfile:
            columns = _empty_columns_for_metadata()
            header = _metadata_headers()

            for line in manifest:
                file_path = line.split("  ")[1].rstrip()
                columns += _file_columns(file_path)
                header += _file_headers()

            outfile.write("\t".join(header))
            outfile.write("\n")
            outfile.write("\t".join(columns))


## Support methods


def _outfile_name(destination):
    return "%sbagout.tsv" %(destination)


def _file_headers():
    return [
        "file_path",
        "file_title",
        "file_visibility",
        "file_embargo_release",
        "file_uri",
        "file_pid",
    ]


def _file_columns(file_path, visibility="restricted"):
    return [file_path, "", visibility, "", "", ""]


def _empty_columns_for_metadata():
    return ["" for x in _metadata_headers()]


def _metadata_headers():
    return [
        "work_type",
        "title",
        "submitter_email",
        "alternate_title",
        "creator",
        "advisors",
        "college",
        "department",
        "subject",
        "degree",
        "date_created",
        "language",
        "alt_description",
        "rights",
        "publisher",
        "note",
        "collection",
        "visibility",
    ]
