# picoCosmo

*python* scritp to analyze data from Cosmo Detectors and Kamiokanne 
 by Netzwerk Teilchenwelt with picoScope USB device

This code relies on

  - the data acquisition and analysis package
    picoDAQ, https://github.com/GuenterQuast/picoDAQ, which 
    must be installed on your system, together with 
  - the  *python* bindings of the *pico-python* project by
    Colin O'Flynn, see https://github.com/colinoflynn/pico-python and 
  - the low-level drivers and C-libraries contained in 
    the Pico Technology Software Development Kit,
    see  https://www.picotech.com/downloads

The code is a specialised version of the example `runDAQ.py`
in package picoDAQ.

`runCosmo` is controlled by an input `.yaml` file specifying
the picoScope configuration and the filter settings:

   ./runCosmo DAQ_xxx.yaml

     - DAQ_Cosmo.yaml : configuration for Cosmo-Panels
     - DAQ_Kanne.yaml : configuration for Kamiokanne

`runCosmo` is tailored to identify short pulses from muon detectors (the 
scintillator panels of the *CosMO*-experiment by "Netzwerk Teilchenwelt",
http://www.teilchenwelt.de, or the Kamiokanne-Experiment with
photomultiplier readout and pulses shaped to a length of approx. 150ns). 

In a first step, the trigger is validated by cross-correlation with a signal template located around the trigger time. Coincidences near a validated triggering pulse are searched for in all connected channels. 
The third step performs a search for additional pulses after the
triggering event, indicating the decay of a stopped muon in or near the detector. This simple set-up allows to measure the mean muon lifetime
in the muon rest frame (2.2 µs). To run the example, connect one, two
or three panels to your PicoScope and type

  `./runCosmo.py DAQ_Cosmo.json` 


In addition to a real-time display of waveforms and rates, raw waveforms
or pictures in `.png`-format of identified double pulses can be stored,
for off-line analysis or for an instructive analysis "by Hand" based
on the waveform pictures.


##Installation

  - Install the PicoTech Software Development Kit from  
    <https://www.picotech.com/library/oscilloscopes/picoscope-software-development-kit-sdk>.
  - Install the `pico-pyhton` package from   
    <https://github.com/colinoflynn/pico-python>.
  - Install the picoDAQ package, vers. >= 0.7.2 from 
    <https://github.com/GuenterQuast/picoDAQ> 
  - Download all files from this project
    <https://github.com/GuenterQuast/picoCosmo> 

## Configuration and program execution
To start the program, type `./runCosmo DAQ_xxxx.yaml`, where  
xxx is the name of the configuration you want to use, either
`Cosmo` for the CosMO panels, or `Kanne` for the "Kamiokanne"   
detector. Control is performed via the main window of the
BufferManager, which contains the options `Pause`, `Resume`,
`Stop` and `EndRun`. In stopped state, all windows remain open
and Graphs may be saved and log-output inspected. In End-state,
all processes are stopped, and consequently all windows disappear.
Resume running from Stop-state is presently not foreseen. 

A helper script, plotDoublePulses.py, allow to read in stored
raw waveforms from the double-pulse search and display as an
oscilloscope display. Code to store each picture as a `.png`
is included, but commented out.

The configuration for the `runCosmo.py` is defined in several '.yaml' files. The fist one contains the overall configuration and specifies
configurations for the oscilloscope, the BufferManager and the Pulse
Filter.  Here is the example to run with Kamiokanne:

    # file DAQ_Kanne.yaml
    # --------------------
    # configuration for runDAQ.py with Kamiokanne 

    DeviceFile:    PMpulse.yaml     # Oscilloscope configuration file
    BMfile:        BMconfig.yaml    # Buffer Manager configuration
    PFfile:        PFconfig.yaml    # Pulse Filter Configuration 

The oscilloscope configuration specifies the oscilloscope model,
 the active channels and the trigger conditions:

    # file PMpulse.yaml
    # -----------------
    # configuration file for PicoScope 2000 Series connected to a PM tube

    PSmodel: 2000a      # model type here (2000a is default)

    picoChannels:      [A]
    ## picoChannels:     [A, B]
    ChanRanges:        [0.5, 0.2]
    ChanOffsets:       [0.4, 0.45]

    sampleTime:   16.E-6  # scientific format with '.' and signed exponent 
    Nsamples:     3500

    trgChan:    A
    trgThr:     -45.E-3
    trgTyp:     Falling
    trgTO:      5000
    pretrig:    0.05
    ChanColors: [darkblue, sienna, indigo]

    frqSG: 0.0  # internal wavefrom generator off

The configuration for the Buffer manager allows to specify the   
display modules for raw data or logging levels:  

    # file BMconfig.yaml
    # ------------------
    # configuration of picoDAQ Buffer Manager 

    NBuffers: 16         # number of buffers to store raw waveforms
    BMmodules: [mpOsci]  # BufferMan modules to start

    verbose: 2   # set verbosity level

    LogFile: BMsum # write log-file entries with current statistics

The configuration for running with the CosMO detectors or Kamiokanne
are specified in the PulseFilter configuration file.  An Example is
shown here: 

    # file PFconfig.yaml
    # -------------------
    # Configuration file for PulseFilter

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
20 days with the Kamiokanne detector. The compressed file `rawDP_180403.dat.zip` contains the raw wave forms of identified double-pulses in `yaml`-format. The script `plotDoublePulses.py` can be used to read the unzipped file and to produce displays of the waveforms. These
pictures are also contained in the compressed file `dpFigs-180403.zip`.
The parameters of events with double-pulses are stored in 
file dpKanne2_180403.dat. An unbinnded logLikelihood fit of measured
lifetimes between 1.5 µs and 15. µs with the script `fit_dpData.py`
yields the result shown in figure `life-ofMU_180403.png`.    




