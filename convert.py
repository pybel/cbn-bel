# -*- coding: utf-8 -*-

"""Export CBN in several BEL formats."""

import os
import sys
import zipfile
from urllib.request import urlretrieve

import click

import pybel
import pybel.grounding
import pybel.struct
from pybel import BELGraph

HERE = os.path.abspath(os.path.dirname(__file__))
HUMAN_PARTS = os.path.join(HERE, 'human_2.0')
os.makedirs(HUMAN_PARTS, exist_ok=True)

BEL = os.path.join(HERE, 'bel')
os.makedirs(BEL, exist_ok=True)

HUMAN_URL = 'http://causalbionet.com/Content/jgf_bulk_files/Human-2.0.zip'
HUMAN_PATH = os.path.join(HERE, 'Human-2.0.zip')


@click.command()
@click.option('--force', is_flag=True)
def main(force: bool):
    """Export CBN in several BEL formats."""
    if not os.path.exists(HUMAN_PATH):
        urlretrieve(HUMAN_URL, HUMAN_PATH)

    full = BELGraph(name='CausalBioNet Human', version='2.0')
    full_nodelink_path = os.path.join(BEL, 'human_2.0.bel.nodelink.json')
    full_bel_path = os.path.join(BEL, 'human_2.0.bel.gz')

    if os.path.exists(full_nodelink_path) and not force:
        click.echo('already done!')
        return sys.exit(0)

    with zipfile.ZipFile(HUMAN_PATH) as human_zipfile:
        for zf in human_zipfile.filelist:
            name = zf.filename[:-len('.jgf')]
            raw_path = os.path.join(HUMAN_PARTS, f'{name}-raw.bel.nodelink.json')
            grounded_path = os.path.join(HUMAN_PARTS, f'{name}-grounded.bel.nodelink.json')

            if os.path.exists(grounded_path) and not force:
                continue

            with human_zipfile.open(zf) as file:
                graph = pybel.from_cbn_jgif_file(file)

            print(zf)

            pybel.dump(graph, raw_path, indent=2)

            graph = pybel.grounding.ground(graph)
            pybel.dump(graph, grounded_path, indent=2)

            pybel.struct.add_annotation_value(graph, 'cbn_pathway', name, strict=False)
            full += graph

    pybel.dump(full, full_nodelink_path, indent=2)
    pybel.dump(full, full_bel_path)


if __name__ == '__main__':
    main()
