# picoCosmo

*python* scritp to analyze data from Cosmo Detectors and Kamiokanne 
 by Netzwerk Teilchenwelt with picoScope USB device

The software is tailored to identify short pulses from muon detectors (the 
scintillator panels of the *CosMO*-experiment by "Netzwerk Teilchenwelt",
<http://www.teilchenwelt.de>, or the *Kamiokanne*-Experiment with
photomultiplier readout ( in the examples shown below the pulses were
shaped to a length of approx. 150 ns). 

In a first step, the trigger is validated by cross-correlation with a 
signal template located around the trigger time. Coincidences near a
validated triggering pulse are searched for in all connected channels. 
The third step performs a search for additional pulses after the
triggering event, indicating the decay of a stopped muon in or near the
detector. This simple set-up allows to measure the mean muon lifetime
in the muon rest frame (2.2 µs). 

Real-time displays of waveforms and rates are provided. In addition, raw
waveforms or pictures in `.png`-format of identified double pulses can
optionally  be stored for off-line analysis or for an instructive analysis "by Hand" based on the waveform pictures.

## Dependence on other packages

This code relies on

  - the data acquisition and analysis package
    picoDAQ, <https://github.com/GuenterQuast/picoDAQ>, which
    must be installed on your system, together with
  - the  *python* bindings of the *pico-python* project by Colin
    O'Flynn, see <https://github.com/colinoflynn/pico-python> and
  - the low-level drivers and C-libraries contained in
    the Pico Technology Software Development Kit, see
    <https://www.picotech.com/downloads>

The code also runs on a Raspberry Pi. 

## Program Execution

The program may be started on the command line (`runCosmo.py`) or via a  
graphical interface (`CosmoGui.py`)
Both are controlled by an input file in `.yaml` format, specifying
configuration of the the PicoScope device, the Buffer Manager and the   
pulse filter:

   ./runCosmo xxx.daq

     - Cosmo.daq : configuration for Cosmo-Panels
     - Kanne.daq : configuration for Kamiokanne
These files contain the names of the files containing the configurations
for the PicoScope device, the Buffer Manager and the Pulse Filter.

The graphical interface can also be initialized with a configuration file:

   ./CosmoGui xxx.daq
Alternatively, the configuration file can be selected and edited in the  
graphical interface. 

The graphical interface allows to inspect and modify the configuration and to start a new run. Configuration and output files are
stored in a newly created directory `<Run Tag>_<date>/`, where a specific `<Run Tag>` can be specified by the user.


##Installation

  - Install the PicoTech Software Development Kit from  
    <https://www.picotech.com/library/oscilloscopes/picoscope-software-development-kit-sdk>.
  - Install the `pico-pyhton` package from   
    <https://github.com/colinoflynn/pico-python>.
  - Install the picoDAQ package, vers. >= 0.7.2 from 
    <https://github.com/GuenterQuast/picoDAQ>. 
  - Download all files from this project
    <https://github.com/GuenterQuast/picoCosmo>.

For your convenience, the sub-directory `whl/` contains
compatible versions of `picoscope` from package `pico-pyhton`
and `picodaqa` from package `picoDAQ` as python-wheels, which
you may install via *pip install package-<vers\>-<tags\>.whl*.

## Configuration and program execution

As stated above, data Acquisition and Analysis is started using the
graphical interface by typing `./CosmoGui.py xxx.daq`, or optionally, 
by directly starting the pyhton script for run execution with the
command `./runCosmo xxxx.daq`.

After run start, control is performed via the main window of the
BufferManager, which contains the options `Pause`, `Resume`,
`Stop` and `EndRun`. In stopped state, all windows remain open
and graphs may be saved and log-output inspected. In End-state,
all processes are stopped, and consequently all windows disappear.
Resume running from Stop-state is presently not foreseen. 

A helper script, plotDoublePulses.py, allow to read in stored
raw waveforms from the double-pulse search and display them as an
oscilloscope display. Code to store each picture as a `.png`
is included, but commented out.

The configuration for the `runCosmo.py` is defined in several '.yaml' files contained in sub-directory `config/`. The files used for
a specific configuration are listed in files of type `.daq`, e.g. `Kanne.daq` for Kamiokanne and `Cosmo.daq` for a run with the 
CosMo panels. 

The  `.yaml` files specify configurations for the oscilloscope, the BufferManager and the Pulse Filter. Here is the example to run with Kamiokanne:

    # file Kanne.daq
    # --------------------
    # configuration files for Kamiokanne 

    DeviceFile: config/PMpulse.yaml   # Oscilloscope configuration file
    BMfile:     config/BMconfig.yaml  # Buffer Manager configuration
    PFfile:     config/PFconfig.yaml  # Pulse Filter Configuration 

The oscilloscope configuration specifies the oscilloscope model,
 the active channels and the trigger conditions:

    # file PMpulse.yaml
    # -----------------
    # configuration file for PicoScope 2000 Series connected to a PM tube

    PSmodel: 2000a      # model type here (2000a is default)

    picoChannels:      [A]
    ChanRanges:        [0.5, 0.2]
    ChanOffsets:       [0.4, 0.45]

    sampleTime:   16.E-6  # scientific format with '.' and signed exponent 
    Nsamples:     3500

    trgChan:    A
    trgThr:     -45.E-3
    trgTyp:     Falling
    trgTO:      5000    #   time-out after which read-out occurs
    pretrig:    0.05
    ChanColors: [darkblue, sienna, indigo]


The configuration for the Buffer manager allows to specify the   
display modules for raw data or logging levels:  

    # file BMconfig.yaml
    # ------------------
    # configuration of picoDAQ Buffer Manager 

    NBuffers: 16         # number of buffers to store raw waveforms
    BMmodules: [mpOsci]  # BufferMan modules to start
    verbose: 1   # set verbosity level
    LogFile: BMsum # write log-file entries with current statistics

The configuration for running with the CosMO detectors or Kamiokanne
are specified in the PulseFilter configuration file.  An Example is
shown here: 

    # file PFconfig.yaml
    # -------------------
    # Configuration file for PulseFilter with Kamiokanne

    #logFile: pFilt     # store all pulses, put Null if no output wanted
    logFile: Null      # store all pulses, put Null if no output wanted
    logFile2: dpFilt   # store double-pulses only, put Null if not
    rawFile:  rawDP    # store raw wave forms, put Null if not wanted
    pictFile: pictDP   # save pictures of double-pulse wave forms

    # pulse parameters
    #         ______
    #        /      \  
    #     _ /_ _ _ _ \_ _ _ _ _ _ _   
    #                 \__________/
    #      r    on  f f2   off  r2 
    #                 f2 - r2 for bi-polar only

    pulseShape:
    # trigger pulse
     - taur   : 20.E-9
       tauon  : 12.E-9 
       tauf   : 128.E-9 
       tauf2  : 0. 
       tauoff : 0. 
       taur2  : 0.
       pheight: -0.045
       mode   : 0             # 0:uni-polar  1: bipolar 

    # other pulses (optional, if not given, use same as for trigger)
     - taur   : 20.E-9
       tauon  : 12.E-9 
       tauf   : 128.E-9 
       tauf2  : 0. 
       tauoff : 0. 
       taur2  : 0.
       pheight: -0.035
       mode   : 0             # 0:uni-polar  1: bipolar 

    # Display Modules to be started
    modules: [RMeter, Display, Hists]

    # Definition of Histograms
    histograms:
     # min  max Nbins ymax    title              lin/log
     - [0., 0.4, 50, 20., "noise Trg. Pulse (V)", 0]
     - [0., 0.8, 50, 15., "valid Trg. Pulse (V)", 0]
     - [0., 15.,  45, 7.5, "Tau (µs)", 1]
     - [0., 0.8, 50, 15., "Pulse Height (V)", 0]

    doublePulse: True  # switch for double-pulse search


## Example output

The directory `./output` contains the results from a long run of almost
20 days with the Kamiokanne detector and a one-day run with the CosMO
panels. The compressed file `rawDP_<date>.dat.zip` contains the 
raw wave forms of identified double-pulses in `yaml`-format. The
script `plotDoublePulses.py` can be used to read the unzipped file and to
produce graphical displays of the waveforms. These pictures are also contained in the compressed file `dpFigs-<date>.zip`. 

The parameters of events containing double-pulses are stored in file
dpKanne2_180403.dat. An unbinned log-likelihood fit of measured
lifetimes between 1.5 µs and 15. µs with the script `fit_dpData.py`
yields the result shown in figure `life-ofMU_180403.png`.    

