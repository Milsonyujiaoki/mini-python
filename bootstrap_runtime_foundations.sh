#!/usr/bin/env bash

set -euo pipefail

ROOT="runtime"

echo "Creating runtime foundations..."

# =========================================================
# CORE RUNTIME MODULES
# =========================================================

MODULES=(
  "pybuiltins"
  "pyobject"
  "pyprotocols"
  "pygenerators"
  "pydescriptors"
  "pycontext"
  "pycallables"
  "pynamespaces"
  "pyexceptions"
  "pymemory"
)

# =========================================================
# COMMON STRUCTURE
# =========================================================

COMMON_DIRS=(
  "docs"
  "examples"
  "research"
  "tests/unit"
  "tests/integration"
  "tests/edge_cases"
  "benchmarks"
)

# =========================================================
# CREATE MODULE STRUCTURE
# =========================================================

for module in "${MODULES[@]}"; do
  echo "Creating module: $module"

  mkdir -p "$ROOT/$module"

  for dir in "${COMMON_DIRS[@]}"; do
    mkdir -p "$ROOT/$module/$dir"
  done

  mkdir -p "$ROOT/$module/src/$module"

  touch "$ROOT/$module/README.md"
  touch "$ROOT/$module/pyproject.toml"

done

# =========================================================
# PYBUILTINS
# =========================================================

mkdir -p runtime/pybuiltins/src/pybuiltins/{iteration,containers,functional,reflection,objectmodel}

touch runtime/pybuiltins/src/pybuiltins/__init__.py

touch runtime/pybuiltins/src/pybuiltins/iteration/{
iter.py,
next.py,
enumerate.py,
zip.py,
map.py,
filter.py,
range.py,
reversed.py,
sorted.py
}

touch runtime/pybuiltins/src/pybuiltins/containers/{
list_object.py,
tuple_object.py,
dict_object.py,
set_object.py
}

touch runtime/pybuiltins/src/pybuiltins/functional/{
all.py,
any.py,
sum.py,
min.py,
max.py
}

touch runtime/pybuiltins/src/pybuiltins/reflection/{
type_builtin.py,
isinstance_builtin.py,
issubclass_builtin.py,
callable_builtin.py,
getattr_builtin.py,
setattr_builtin.py
}

touch runtime/pybuiltins/src/pybuiltins/objectmodel/{
object_base.py,
super_builtin.py,
property_builtin.py,
classmethod_builtin.py,
staticmethod_builtin.py
}

# =========================================================
# PYOBJECT
# =========================================================

mkdir -p runtime/pyobject/src/pyobject/{model,attributes,slots,identity}

touch runtime/pyobject/src/pyobject/__init__.py

touch runtime/pyobject/src/pyobject/model/{
object_model.py,
attribute_lookup.py,
method_resolution.py
}

touch runtime/pyobject/src/pyobject/attributes/{
getattribute.py,
getattr.py,
setattr.py,
delattr.py
}

touch runtime/pyobject/src/pyobject/slots/{
slots.py,
memory_layout.py
}

touch runtime/pyobject/src/pyobject/identity/{
identity.py,
mutability.py,
references.py
}

# =========================================================
# PYPROTOCOLS
# =========================================================

mkdir -p runtime/pyprotocols/src/pyprotocols/{iteration,containers,operators,context,async_protocols}

touch runtime/pyprotocols/src/pyprotocols/__init__.py

touch runtime/pyprotocols/src/pyprotocols/iteration/{
iter_protocol.py,
next_protocol.py
}

touch runtime/pyprotocols/src/pyprotocols/containers/{
getitem.py,
setitem.py,
contains.py,
len_protocol.py
}

touch runtime/pyprotocols/src/pyprotocols/operators/{
numeric.py,
comparison.py,
representation.py
}

touch runtime/pyprotocols/src/pyprotocols/context/{
enter_exit.py
}

touch runtime/pyprotocols/src/pyprotocols/async_protocols/{
await_protocol.py,
aiter_protocol.py,
anext_protocol.py
}

# =========================================================
# PYGENERATORS
# =========================================================

mkdir -p runtime/pygenerators/src/pygenerators/{core,coroutines,state_machine}

touch runtime/pygenerators/src/pygenerators/__init__.py

touch runtime/pygenerators/src/pygenerators/core/{
yield_mechanics.py,
yield_from.py,
generator_states.py
}

touch runtime/pygenerators/src/pygenerators/coroutines/{
coroutines.py,
cooperative_execution.py
}

touch runtime/pygenerators/src/pygenerators/state_machine/{
suspension.py,
execution_resume.py
}

# =========================================================
# PYDESCRIPTORS
# =========================================================

mkdir -p runtime/pydescriptors/src/pydescriptors/{core,properties,methods}

touch runtime/pydescriptors/src/pydescriptors/__init__.py

touch runtime/pydescriptors/src/pydescriptors/core/{
descriptor_protocol.py,
data_descriptors.py,
non_data_descriptors.py
}

touch runtime/pydescriptors/src/pydescriptors/properties/{
property_descriptor.py
}

touch runtime/pydescriptors/src/pydescriptors/methods/{
bound_methods.py,
classmethod_descriptor.py,
staticmethod_descriptor.py
}

# =========================================================
# PYCONTEXT
# =========================================================

mkdir -p runtime/pycontext/src/pycontext/{sync,async}

touch runtime/pycontext/src/pycontext/__init__.py

touch runtime/pycontext/src/pycontext/sync/{
context_manager.py,
resource_management.py
}

touch runtime/pycontext/src/pycontext/async/{
async_context_manager.py
}

# =========================================================
# PYCALLABLES
# =========================================================

mkdir -p runtime/pycallables/src/pycallables/{functions,closures,decorators}

touch runtime/pycallables/src/pycallables/__init__.py

touch runtime/pycallables/src/pycallables/functions/{
call_protocol.py,
function_objects.py
}

touch runtime/pycallables/src/pycallables/closures/{
closures.py,
free_variables.py,
cell_objects.py
}

touch runtime/pycallables/src/pycallables/decorators/{
function_decorators.py,
class_decorators.py
}

# =========================================================
# PYNAMESPACES
# =========================================================

mkdir -p runtime/pynamespaces/src/pynamespaces/{scope,lookup}

touch runtime/pynamespaces/src/pynamespaces/__init__.py

touch runtime/pynamespaces/src/pynamespaces/scope/{
legb_rule.py,
global_scope.py,
local_scope.py,
enclosed_scope.py
}

touch runtime/pynamespaces/src/pynamespaces/lookup/{
name_resolution.py
}

# =========================================================
# PYEXCEPTIONS
# =========================================================

mkdir -p runtime/pyexceptions/src/pyexceptions/{hierarchy,traceback,handling}

touch runtime/pyexceptions/src/pyexceptions/__init__.py

touch runtime/pyexceptions/src/pyexceptions/hierarchy/{
base_exception.py,
exception_tree.py
}

touch runtime/pyexceptions/src/pyexceptions/traceback/{
traceback_objects.py,
stack_frames.py
}

touch runtime/pyexceptions/src/pyexceptions/handling/{
try_except.py,
exception_chaining.py
}

# =========================================================
# PYMEMORY
# =========================================================

mkdir -p runtime/pymemory/src/pymemory/{references,gc,internals}

touch runtime/pymemory/src/pymemory/__init__.py

touch runtime/pymemory/src/pymemory/references/{
reference_counting.py,
weak_references.py
}

touch runtime/pymemory/src/pymemory/gc/{
garbage_collection.py,
cyclic_gc.py
}

touch runtime/pymemory/src/pymemory/internals/{
memory_layout.py,
object_headers.py
}

echo "Runtime foundations created successfully."
