# Copyright 2020 Google LLC
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     https://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
FROM gcr.io/kctf-docker/kctf-nsjail-chroot:latest AS chroot
FROM gcr.io/kctf-docker/kctf-nsjail-bin:latest AS bin
FROM ubuntu:20.04

RUN apt-get update \
    && apt-get install -yq --no-install-recommends uidmap libprotobuf17 libnl-route-3-200 wget netcat ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN /usr/sbin/useradd --no-create-home -u 1000 user

COPY --from=bin /usr/bin/nsjail /usr/bin/nsjail
COPY --from=chroot /chroot /chroot

# create a python3 venv and install ecdsa for the proof-of-work
RUN apt-get update && apt-get -y install python3-venv
RUN python3 -m venv --copies /venv
RUN bash -c "source /venv/bin/activate && pip3 install ecdsa"
RUN mv /venv /chroot/

RUN mkdir /kctf
RUN mkdir -p /kctf/.fullproc/proc
RUN chmod 0700 /kctf/.fullproc
RUN mkdir /chroot/.kctf
RUN mkdir /chroot/.kctf/pow
RUN mkdir /chroot/.kctf/pow-bypass

COPY files/kctf_setup /usr/bin/
COPY files/drop_privs /usr/bin/
COPY files/proof_of_work/pow.py /chroot/usr/bin/
COPY files/proof_of_work/maybe_pow.sh /chroot/usr/bin/
COPY files/nsjail_base.cfg /kctf/nsjail_base.cfg
