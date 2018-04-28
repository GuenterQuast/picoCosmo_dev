# picoCosmo

*python* scritp to analyze date from Cosmo Detectors and Kamiokanne 
 by Netzwerk Teilchenwelt with picoScope USB device

This code relies on

  - the data acquisition and analysis package
    picoDAQ, https://github.com/GuenterQuast/picoDAQ), which 
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

     - DAQ_Cosmon.yaml : configuration for Cosmo-Panels
     - DAQ_Kanne.yaml : configuration for Kamiokanne

`runCosmo` is tailored to identify short pulses from muon detectors (the scintillator panels of the *CosMO*-experiment by "Netzwerk Teilchenwelt",
http://www.teilchenwelt.de, or the Kamiokanne-Experiment with
photomultiplier readout and pulses shaped to a length of approx. 150ns). 

In a first step, the trigger is validated by cross-correlation with a signal template located around the trigger time. Coincidences near a validated triggering pulse are searched for in all connected channels. The third step
performs a search for additional pulses after the triggering event, indicating
the decay of a stopped muon in or near the detector. This simple set-up allows
to measure the mean muon lifetime in the muon rest frame (2.2 µs). To run the
example, connect one, two or three panels to your PicoScope and type

  `./runCosmo.py DAQ_Cosmo.json` 

In addition to a real-time display of waveforms and rates raw waveforms or
pictures in .png-format of identified double pulses can be stored, for 
off-line analysis or for an an instructive analysis "by Hand" based on the
waveform pictures.
