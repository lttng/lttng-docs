---
id: oe-yocto
---

LTTng recipes are available in the `openembedded-core` layer of
OpenEmbedded:

  * `lttng-tools`
  * `lttng-modules`
  * `lttng-ust`

Using BitBake, the simplest way to include LTTng recipes in your
target image is to add them to `IMAGE_INSTALL_append` in
`conf/local.conf`:

~~~ text
IMAGE_INSTALL_append = " lttng-tools lttng-modules lttng-ust"
~~~

If you're using Hob, click _Edit image recipe_ once you have selected
a machine and an image recipe. Then, in the _All recipes_ tab, search
for `lttng` and you should find and be able to include the three LTTng
recipes.
