# spike-uart

Spiking hardware implementation of UART serial comms.

# References

- James Sharman, YouTube - [Receive - UART from Scratch](https://www.youtube.com/watch?v=Bqc7YsC1f1Q&t=2s)
- James Sharman, YouTube -  [Transmit - UART from Scratch](https://www.youtube.com/watch?v=aE5VTp_eMN4)

## Demo

Receive - UART Circuit

[![Receive - UART Circuit](https://github.com/JimKnowler/spike-uart/raw/master/docs/uart-receive..gif)](https://github.com/JimKnowler/spike-uart/raw/master/docs/uart-receive.mp4)

Receive - UART Circuit in Oscilloscope

[![Receive - UART Circuit in Oscilloscope](https://github.com/JimKnowler/spike-uart/raw/master/docs/oscilloscope-receive.gif)](https://github.com/JimKnowler/spike-uart/raw/master/docs/oscilloscope-receive.mp4)

## Requirements

- python3

- pyserial
  > pip3 install pyserial

- USB / serial cable
  - https://www.amazon.co.uk/gp/product/B01N4X3BJB/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1

## Scan for serial port

> python3 -m serial.tools.list_ports

##