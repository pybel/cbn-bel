BEL Export of Causal Biological Networks Database
======================
This repository contains exports of the `Causal Biologial Networks Database (CBN) <http://causalbionet.com>`_
as `Biological Expression Language (BEL) <http://bel.bio>`_. The research article describing
the CBN is:

  `Causal biological network database: A comprehensive platform of causal biological network models focused on the
  pulmonary and vascular systems <https://doi.org/10.1007/978-1-4939-2778-4_3>`_. Talikka, M., Boue, S., & Schlage,
  W. K. *Computational Systems Toxicology* (2015) 65–93. DOI: 10.1007/978-1-4939-2778-4_3

BEL is a domain specific language that enables the expression of biological relationships
in a machine-readable format. It is supported by the `PyBEL <https://github.com/pybel/pybel>`_
software ecosystem.

Download CBN as BEL
-------------------
The network is available in two BEL formats in the `/bel <https://github.com/pybel/cbn-bel/tree/master/bel>`_
directory:

- **BEL Script** - see description `below <https://github.com/pybel/cbn-bel#bel-script>`_
- **Nodelink JSON** - see description `below <https://github.com/pybel/cbn-bel#nodelink-json>`_

In the `human_2.0 <https://github.com/pybel/cbn-bel/tree/master/human_2.0>`_, you can also find the
networks in both the raw and grounded formats. These are ultimately combine to make the full exports
in the ``bel/`` directory. All edges maintain tags as to their provenance from which network they came.

License
-------
This repository and its maintainers are not affiliated with the content creators at sbv IMPROVER project
nor Philip Morris International, but they have graciously allowed us to redistribute their content with the
following message:

The sbv IMPROVER project, the website and the Symposia are part of a collaborative project
designed to enable scientists to learn about and contribute to the development of a new crowd
sourcing method for verification of scientific data and results. The current challenges, website
and biological network models were developed and are maintained as part of a collaboration among
Selventa, OrangeBus and ADS. The project is led and funded by Philip Morris International. For more
information on the focus of Philip Morris International’s research, please visit www.pmi.com.

Please cite:

- http://www.causalbionet.com
- https://bionet.sbvimprover.com

as well as any relevant publications.

Format Descriptions
-------------------
BEL Script
~~~~~~~~~~
BEL Script is the *de facto* standard for BEL, which all BEL-aware applications should be able to consume.
It contains informations about the nodes, edges, and their biological context in a domain-specific language.
It can be parsed with PyBEL or other BEL parsers.

Example opening BEL Script using `pybel.from_bel_script_gz() <https://pybel.readthedocs.io/en/latest/reference/io.html#pybel.from_bel_script_gz>`_:

.. code-block:: python

    from pybel import from_bel_script_gz
    graph = from_bel_script_gz('human_2.0.bel.gz')

Nodelink JSON
~~~~~~~~~~~~~
Node-link is the format popularized by Javascript frameworks like D3 for representing network
information. Since the main data structire in PyBEL is a network, it often makes sense to use
Nodelink JSON as a pre-compiled data structure for BEL (since parsing/compiling BEL takes a
lot longer than JSON). The schema is specific to PyBEL, but this is the fastest to load.

Example opening Nodelink JSON using `pybel.from_nodelink_gz()
<https://pybel.readthedocs.io/en/latest/reference/io.html#pybel.from_nodelink_gz>`_:

.. code-block:: python

    from pybel import from_nodelink_gz
    graph = from_nodelink_gz('human_2.0.bel.nodelink.json.gz')
