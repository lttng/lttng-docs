---
id: prebuilt-ust-helpers
---

The LTTng-UST package provides a few helpers that one may find
useful in some situations. They all work the same way: you must
preload the appropriate shared object before running the user
application (using the `LD_PRELOAD` environment variable).

The shared objects are normally found in `/usr/lib`.

The current installed helpers are:

  * `liblttng-ust-libc-wrapper.so` and
    `liblttng-ust-pthread-wrapper.so`:
    [C&nbsp;standard library and POSIX threads tracing](#doc-liblttng-ust-libc-pthread-wrapper)
  * `liblttng-ust-cyg-profile.so` and
    `liblttng-ust-cyg-profile-fast.so`:
    [function tracing](#doc-liblttng-ust-cyg-profile)
  * `liblttng-ust-dl.so`:
    [dynamic linker tracing](#doc-liblttng-ust-dl)

The following subsections document what helpers instrument exactly
and how to use them.
