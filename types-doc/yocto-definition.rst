YOCTO Linux
-----------
``yocto`` for Yocto Linux recipes:

There is no default package repository. The classifier `repository_url` is optional.

:namespace: The namespace is the name of the layer which provides the recipe. The layer name as
specified in the `BBFILE_COLLECTIONS` variable in `conf/layer.conf` of the layer.
:name: The name of the package also known as [PN](https://docs.yoctoproject.org/ref-manual/variables.html#term-PN) in a yocto recipe.
:version: The version of the package also known as [PV](https://docs.yoctoproject.org/ref-manual/variables.html#term-PV) in a yocto recipe.

Qualifiers
^^^^^^^^^^
All qualifiers should be percent-encoded.

``repository_url``
  The GIT URL of the layer.
  In example:

  * ``https%3A%2F%2Fgit.openembedded.org%2Fopenembedded-core``
  * ``https%3A%2F%2Fgithub.com%2Fakuster%2Fmeta-odroid``

  The protocol can be ``https``, ``ssh``  or ``git`` and is mandatory.

``layer_version``
  layer_version is the version of the yocto layer which is a SHA1 commit, tag or branch
  of the yocto layer GIT repository. It should support also [short commits](https://git-scm.com/book/en/v2/Git-Tools-Revision-Selection#_short_sha_1). (optional)

Examples
^^^^^^^^

::

  pkg:yocto/openembedded-core/glibc@2.35
  pkg:yocto/openembedded-core/glibc@2.35&repository_url=https%3A%2F%2Fgit.openembedded.org%2Fopenembedded-core&layer_version=kirkstone
  pkg:yocto/openembedded-core/glibc@2.35&repository_url=https%3A%2F%2Fgit.openembedded.org%2Fopenembedded-core&layer_version=25ba9895b9
  pkg:yocto/openembedded-core/glibc@2.35&repository_url=https%3A%2F%2Fgit.openembedded.org%2Fopenembedded-core&layer_version=25ba9895b98715adb66a06e50f644aea2e2c9eb6
  pkg:yocto/meta-xilinx-core/u-boot-xlnx-uenv@1.0.0
  pkg:yocto/meta-odroid/emmc@1.0.0?layer_version=4e07fab&repository_url=https%3A%2F%2Fgithub.com%2Fakuster%2Fmeta-odroid
