#! /usr/bin/env python

# Programs that are runnable.
ns3_runnable_programs = ['build/src/aodv/examples/ns3.19-aodv-debug', 'build/src/bridge/examples/ns3.19-csma-bridge-debug', 'build/src/bridge/examples/ns3.19-csma-bridge-one-hop-debug', 'build/src/buildings/examples/ns3.19-buildings-pathloss-profiler-debug', 'build/src/config-store/examples/ns3.19-config-store-save-debug', 'build/src/core/examples/ns3.19-main-callback-debug', 'build/src/core/examples/ns3.19-sample-simulator-debug', 'build/src/core/examples/ns3.19-main-ptr-debug', 'build/src/core/examples/ns3.19-main-random-variable-debug', 'build/src/core/examples/ns3.19-main-random-variable-stream-debug', 'build/src/core/examples/ns3.19-sample-random-variable-debug', 'build/src/core/examples/ns3.19-sample-random-variable-stream-debug', 'build/src/core/examples/ns3.19-command-line-example-debug', 'build/src/core/examples/ns3.19-hash-example-debug', 'build/src/core/examples/ns3.19-main-test-sync-debug', 'build/src/csma/examples/ns3.19-csma-one-subnet-debug', 'build/src/csma/examples/ns3.19-csma-broadcast-debug', 'build/src/csma/examples/ns3.19-csma-packet-socket-debug', 'build/src/csma/examples/ns3.19-csma-multicast-debug', 'build/src/csma/examples/ns3.19-csma-raw-ip-socket-debug', 'build/src/csma/examples/ns3.19-csma-ping-debug', 'build/src/csma-layout/examples/ns3.19-csma-star-debug', 'build/src/dsdv/examples/ns3.19-dsdv-manet-debug', 'build/src/dsr/examples/ns3.19-dsr-debug', 'build/src/emu/examples/ns3.19-emu-udp-echo-debug', 'build/src/emu/examples/ns3.19-emu-ping-debug', 'build/src/energy/examples/ns3.19-li-ion-energy-source-debug', 'build/src/fd-net-device/examples/ns3.19-dummy-network-debug', 'build/src/fd-net-device/examples/ns3.19-fd2fd-onoff-debug', 'build/src/fd-net-device/examples/ns3.19-realtime-dummy-network-debug', 'build/src/fd-net-device/examples/ns3.19-realtime-fd2fd-onoff-debug', 'build/src/fd-net-device/examples/ns3.19-fd-emu-ping-debug', 'build/src/fd-net-device/examples/ns3.19-fd-emu-udp-echo-debug', 'build/src/fd-net-device/examples/ns3.19-fd-emu-onoff-debug', 'build/src/fd-net-device/examples/ns3.19-fd-tap-ping-debug', 'build/src/fd-net-device/examples/ns3.19-fd-tap-ping6-debug', 'build/src/internet/examples/ns3.19-main-simple-debug', 'build/src/lte/examples/ns3.19-lena-cqi-threshold-debug', 'build/src/lte/examples/ns3.19-lena-dual-stripe-debug', 'build/src/lte/examples/ns3.19-lena-fading-debug', 'build/src/lte/examples/ns3.19-lena-intercell-interference-debug', 'build/src/lte/examples/ns3.19-lena-pathloss-traces-debug', 'build/src/lte/examples/ns3.19-lena-profiling-debug', 'build/src/lte/examples/ns3.19-lena-rem-debug', 'build/src/lte/examples/ns3.19-lena-rem-sector-antenna-debug', 'build/src/lte/examples/ns3.19-lena-rlc-traces-debug', 'build/src/lte/examples/ns3.19-lena-simple-debug', 'build/src/lte/examples/ns3.19-lena-simple-epc-debug', 'build/src/lte/examples/ns3.19-lena-x2-handover-debug', 'build/src/lte/examples/ns3.19-lena-x2-handover-measures-debug', 'build/src/mesh/examples/ns3.19-mesh-debug', 'build/src/mobility/examples/ns3.19-main-grid-topology-debug', 'build/src/mobility/examples/ns3.19-main-random-topology-debug', 'build/src/mobility/examples/ns3.19-main-random-walk-debug', 'build/src/mobility/examples/ns3.19-mobility-trace-example-debug', 'build/src/mobility/examples/ns3.19-ns2-mobility-trace-debug', 'build/src/mobility/examples/ns3.19-bonnmotion-ns2-example-debug', 'build/src/mpi/examples/ns3.19-simple-distributed-debug', 'build/src/mpi/examples/ns3.19-third-distributed-debug', 'build/src/mpi/examples/ns3.19-nms-p2p-nix-distributed-debug', 'build/src/mpi/examples/ns3.19-simple-distributed-empty-node-debug', 'build/src/netanim/examples/ns3.19-dumbbell-animation-debug', 'build/src/netanim/examples/ns3.19-grid-animation-debug', 'build/src/netanim/examples/ns3.19-star-animation-debug', 'build/src/netanim/examples/ns3.19-wireless-animation-debug', 'build/src/netanim/examples/ns3.19-uan-animation-debug', 'build/src/netanim/examples/ns3.19-dynamic_linknode-debug', 'build/src/network/examples/ns3.19-main-packet-header-debug', 'build/src/network/examples/ns3.19-main-packet-tag-debug', 'build/src/network/examples/ns3.19-red-tests-debug', 'build/src/network/examples/ns3.19-droptail_vs_red-debug', 'build/src/nix-vector-routing/examples/ns3.19-nix-simple-debug', 'build/src/nix-vector-routing/examples/ns3.19-nms-p2p-nix-debug', 'build/src/olsr/examples/ns3.19-simple-point-to-point-olsr-debug', 'build/src/olsr/examples/ns3.19-olsr-hna-debug', 'build/src/point-to-point/examples/ns3.19-main-attribute-value-debug', 'build/src/propagation/examples/ns3.19-main-propagation-loss-debug', 'build/src/propagation/examples/ns3.19-jakes-propagation-model-example-debug', 'build/src/sixlowpan/examples/ns3.19-example-sixlowpan-debug', 'build/src/spectrum/examples/ns3.19-adhoc-aloha-ideal-phy-debug', 'build/src/spectrum/examples/ns3.19-adhoc-aloha-ideal-phy-matrix-propagation-loss-model-debug', 'build/src/spectrum/examples/ns3.19-adhoc-aloha-ideal-phy-with-microwave-oven-debug', 'build/src/stats/examples/ns3.19-gnuplot-example-debug', 'build/src/stats/examples/ns3.19-double-probe-example-debug', 'build/src/stats/examples/ns3.19-gnuplot-aggregator-example-debug', 'build/src/stats/examples/ns3.19-gnuplot-helper-example-debug', 'build/src/stats/examples/ns3.19-file-aggregator-example-debug', 'build/src/stats/examples/ns3.19-file-helper-example-debug', 'build/src/tap-bridge/examples/ns3.19-tap-csma-debug', 'build/src/tap-bridge/examples/ns3.19-tap-csma-virtual-machine-debug', 'build/src/tap-bridge/examples/ns3.19-tap-wifi-virtual-machine-debug', 'build/src/tap-bridge/examples/ns3.19-tap-wifi-dumbbell-debug', 'build/src/topology-read/examples/ns3.19-topology-read-debug', 'build/src/uan/examples/ns3.19-uan-cw-example-debug', 'build/src/uan/examples/ns3.19-uan-rc-example-debug', 'build/src/virtual-net-device/examples/ns3.19-virtual-net-device-debug', 'build/src/wave/examples/ns3.19-wave-simple-80211p-debug', 'build/src/wifi/examples/ns3.19-wifi-phy-test-debug', 'build/src/wimax/examples/ns3.19-wimax-ipv4-debug', 'build/src/wimax/examples/ns3.19-wimax-multicast-debug', 'build/src/wimax/examples/ns3.19-wimax-simple-debug', 'build/examples/realtime/ns3.19-realtime-udp-echo-debug', 'build/examples/socket/ns3.19-socket-bound-static-routing-debug', 'build/examples/socket/ns3.19-socket-bound-tcp-static-routing-debug', 'build/examples/socket/ns3.19-socket-options-ipv4-debug', 'build/examples/socket/ns3.19-socket-options-ipv6-debug', 'build/examples/error-model/ns3.19-simple-error-model-debug', 'build/examples/udp-client-server/ns3.19-udp-client-server-debug', 'build/examples/udp-client-server/ns3.19-udp-trace-client-server-debug', 'build/examples/tutorial/ns3.19-hello-simulator-debug', 'build/examples/tutorial/ns3.19-first-debug', 'build/examples/tutorial/ns3.19-second-debug', 'build/examples/tutorial/ns3.19-third-debug', 'build/examples/tutorial/ns3.19-fourth-debug', 'build/examples/tutorial/ns3.19-fifth-debug', 'build/examples/tutorial/ns3.19-sixth-debug', 'build/examples/tutorial/ns3.19-seventh-debug', 'build/examples/routing/ns3.19-dynamic-global-routing-debug', 'build/examples/routing/ns3.19-static-routing-slash32-debug', 'build/examples/routing/ns3.19-global-routing-slash32-debug', 'build/examples/routing/ns3.19-global-injection-slash32-debug', 'build/examples/routing/ns3.19-simple-global-routing-debug', 'build/examples/routing/ns3.19-simple-alternate-routing-debug', 'build/examples/routing/ns3.19-mixed-global-routing-debug', 'build/examples/routing/ns3.19-simple-routing-ping6-debug', 'build/examples/routing/ns3.19-manet-routing-compare-debug', 'build/examples/tcp/ns3.19-tcp-large-transfer-debug', 'build/examples/tcp/ns3.19-tcp-nsc-lfn-debug', 'build/examples/tcp/ns3.19-tcp-nsc-zoo-debug', 'build/examples/tcp/ns3.19-tcp-star-server-debug', 'build/examples/tcp/ns3.19-star-debug', 'build/examples/tcp/ns3.19-tcp-bulk-send-debug', 'build/examples/tcp/ns3.19-tcp-nsc-comparison-debug', 'build/examples/tcp/ns3.19-tcp-variants-comparison-debug', 'build/examples/naming/ns3.19-object-names-debug', 'build/examples/wireless/ns3.19-mixed-wireless-debug', 'build/examples/wireless/ns3.19-wifi-adhoc-debug', 'build/examples/wireless/ns3.19-wifi-clear-channel-cmu-debug', 'build/examples/wireless/ns3.19-wifi-ap-debug', 'build/examples/wireless/ns3.19-wifi-wired-bridging-debug', 'build/examples/wireless/ns3.19-simple-wifi-frame-aggregation-debug', 'build/examples/wireless/ns3.19-multirate-debug', 'build/examples/wireless/ns3.19-wifi-simple-adhoc-debug', 'build/examples/wireless/ns3.19-wifi-simple-adhoc-grid-debug', 'build/examples/wireless/ns3.19-wifi-simple-infra-debug', 'build/examples/wireless/ns3.19-wifi-simple-interference-debug', 'build/examples/wireless/ns3.19-wifi-blockack-debug', 'build/examples/wireless/ns3.19-ofdm-validation-debug', 'build/examples/wireless/ns3.19-wifi-hidden-terminal-debug', 'build/examples/wireless/ns3.19-ht-wifi-network-debug', 'build/examples/stats/ns3.19-wifi-example-sim-debug', 'build/examples/matrix-topology/ns3.19-matrix-topology-debug', 'build/examples/udp/ns3.19-udp-echo-debug', 'build/examples/energy/ns3.19-energy-model-example-debug', 'build/examples/ipv6/ns3.19-icmpv6-redirect-debug', 'build/examples/ipv6/ns3.19-ping6-debug', 'build/examples/ipv6/ns3.19-radvd-debug', 'build/examples/ipv6/ns3.19-radvd-two-prefix-debug', 'build/examples/ipv6/ns3.19-test-ipv6-debug', 'build/examples/ipv6/ns3.19-fragmentation-ipv6-debug', 'build/examples/ipv6/ns3.19-fragmentation-ipv6-two-MTU-debug', 'build/examples/ipv6/ns3.19-loose-routing-ipv6-debug', 'build/scratch/ns3.19-scratch-simulator-debug', 'build/scratch/ns3.19-myfirst-debug', 'build/scratch/subdir/ns3.19-subdir-debug']

# Scripts that are runnable.
ns3_runnable_scripts = ['csma-bridge.py', 'sample-simulator.py', 'wifi-olsr-flowmon.py', 'tap-csma-virtual-machine.py', 'tap-wifi-virtual-machine.py', 'realtime-udp-echo.py', 'first.py', 'simple-routing-ping6.py', 'mixed-wireless.py', 'wifi-ap.py']

