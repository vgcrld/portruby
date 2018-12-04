#!/bin/sh

# Standard Error Routine
_error() {
  printf "ERROR --- $*\n"
  exit 1
}

# For Oracle OCI8
export LD_LIBRARY_PATH=/usr/lib/oracle/12.1/client64/lib

# Setup
cd $(dirname $0)
_base="$(pwd)"
_name="portruby"
_build_step="${1:-b}"
_targets="x86_64-redhat-linux"

# Remove the old BUILD and BUILDROOT
[ -d "${_base}/BUILD" ] && rm -f -r "${_base}/BUILD"
[ -d "${_base}/BUILDROOT" ] && rm -f -r "${_base}/BUILDROOT"

# Recreate the BUILD and BUILDROOT
mkdir "${_base}/BUILD"
mkdir "${_base}/BUILDROOT"

for _target in ${_targets}; do

  rpmbuild --define="_binary_payload w9.gzdio" \
           --define="_binary_filedigest_algorithm 1" \
           --define="_topdir ${_base}" \
           --define="_tmppath ${_base}/tmp" \
           --target=${_target} \
           -b${_build_step} \
           ${_base}/SPECS/${_name}.spec

  [ $? -ne 0 ] && _error "Could not setup/build RPM for ${_target}"

done
