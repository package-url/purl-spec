YOCTO Linux
-----------
``yocto`` for Yocto Linux recipes:

The default repository is: ``git.yoctoproject.org``

:namespace: The namespace is the name of the layer which provides the recipe.
:name: The name is the name of the recipe.
:version: The version is a commit or tag

Qualifiers
^^^^^^^^^^
``repository``
  The base repository.
  In example:
  
  * ``github.com/Xilinx``
  * ``github.com/openembedded``
  
  The protocol can be ``https`` or ``git`` but is not mandatory.
  **Default:** ``git.yoctoproject.org``

``PV``
  PV is the version of the package itself.
``arch``
  Optional for the architecture like ``mips64`` or ``arm64``

Subpath
^^^^^^^
The subpath is mandatory if the recipe is not in the root direcotry of the
repository.

Examples
^^^^^^^^

::

  pkg:yocto/poky/python-3dbus@f1ad013?PV=1.2.18#meta/recipes-devtools/python
  pkg:yocto/openembedded-core/glibc@9400e1e9208b0f9075dfdfce0a3d1318a7fe6bf4?PV=2.35&repository=git.openembedded.org#meta/recipes-core/
  pkg:yocto/meta-xilinx-core/u-boot-zynq-uenv@06e35a4#recipes-bsp/u-boot/
  pkg:yocto/meta-odroid/emmc@4e07fab?PV=1.0.0&repository=github.com/akuster#recipes-bsp/
