tsidtutorial() {
  export PATH=/opt/openrobots/bin:$PATH
  export LD_LIBRARY_PATH=/opt/openrobots/lib:$LD_LIBRARY_PATH
  export PKG_CONFIG_PATH=/opt/openrobots/lib/pkgconfig:$PKG_CONFIG_PATH
  export CMAKE_PREFIX_PATH=/opt/openrobots:$CMAKE_PREFIX_PATH
  export PYTHONPATH=~/tsid_ws:/opt/openrobots/lib/python3.8/site-packages:$PYTHONPATH
  cd ~/tsid_ws
}
