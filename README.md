# ScuttleTechGuide
SCUTTLE Technical Guide

[Github Repo](https://github.com/dmalawey/ScuttleTechGuide ':class=button')
[Website](https://docsify-this.net/?basePath=https://raw.githubusercontent.com/dmalawey/ScuttleTechGuide/main&sidebar=true#/?show-page-options=true ':class=button')

---

:warning: This document is in draft form as of the latest update

<iframe frameborder="0" style="width:100%;height:387px;" src="diagram/myEmbed.html">
</iframe>


---

<iframe frameborder="0" style="width:100%;height:387px;" src="https://viewer.diagrams.net/?highlight=0000ff&nav=1&title=open%20source%20inverted%20pyramid.drawio#R7Zpbb%2BMoFIB%2FTR9rATa%2BPDZpsl2po6mmHW07LxWJicOUmAiT2%2F76BRvHdi6tm6TNjGZTyYUDHGzOdw4HJxdud7L8S5Lp%2BIuIKb9AIF5euNcXCEEPhvqfkawKSYisIJEsLkSgEtyzf6kdWUpnLKaZlRUiJQRXbNoUDkWa0qFqyIiUYtHsNhI8bgimJKFbgvsh4dvSf1isxlYK%2FahquKEsGZdT%2B9grWiak7G0fJRuTWCxqIrd34XalEKooTZZdys3qNRemv6d1fWeSpqrNANyJp%2FMfdx1%2FNE2eX76yp%2Fsv2aXVMid8Zp%2F4hsh4oZXam1arcimkmKUxNcrghdtZjJmi91MyNK0LbXwtG6sJt80JJ1lmy5mS4oV2BRcy1%2BSC%2FKNbRiJVfTJh3NBxQ%2FmcKjYktsHCAH1bLxXEdERmXBkp47ymtuebPy3XMCjCUirtDRDOklSXh3qljLAzp9JMxK9sw0AoJSa6gZMB5XciY4qJnSNuNzooYR7cLqLuQ5d7rQPXNtfeQsWEKrnSXewABCw31lGQFzm4kCwq8NzAysZ15kJQdiUW92Stfz3lN%2B0eJE20Nd85p%2B9vT4k25iNcL1NKFO0YSLI6h7pQe95KlNOZV79nVH4d%2FDTui0BugUJpj2uRFCkbFgoBZ%2BlL0TRWygSAKzML6i8WCycbzpTiVAptS0fIRIslzcRMakBRPw8jpieTLE0uy2ql9oHIhNqHex5woifK20rnIZPnYEqvw97sx%2Brx75ve4GkGLqFbW1%2FrbYc6TMMVbmdDFhOtrSvSTBh9m6zHIQCBu8u5rjAAHtjwGS0f5Z8N12wF7v7A8QrNgQPCCGONbBgCHPkN0CAATghxiF3fXraogxA6kQdQFGIQeD4qA26dQhc7CEYYri%2F7naBBY4Wertboe5XGfG87DsTMzG7VHM2edzb2CAJAB4Ad7Pn9WmA%2FH3uhUyMvAG4zyGEHRG4EkGcvvz56zS35CPjmOuyJHD5Xl3MlPpkYGsyuW9WUtj%2FGHXO51vIoOhJW%2F4SsNln0vcAPg10sutBzdS7WZG4fl295wIexCh2vjipsbsgYOxEEUYD9%2FAIPQhUjJ0QR8qvLKVjdSi93Gh5vZZE01vm1reqVY2r1jXJisqle1dLRufLU9LBpvbFXp4mJkGosEpHqlEyYHCwX%2FqRKrWzeSGZKNNGhS6Yea%2BUnXTaZU1G7NiYBZWVVVlK9Mo%2F1Sm2UqVbD8lo5LvfeDhm%2BJPltb%2BeuTV435eVZA7VNkjfhrhTSNL4yByGzmsYT2HDNs7HFATRrexZ51RsOr49qtWDxdgZVcw%2BZMzFv3t0rye2dYKmq3Aq60MGVU4R%2BM%2F2IgLOZwBZPZNW8J3lt5wfe7%2B4H%2F%2FPcjmfvz%2BAZHsjzmaN28FbY3qa16W0tOGuLlLuN1HsSiNZE7dnS29kZ%2FZ52%2FrXNvLNf9DFm3nekuO9%2Bf3i47R10ojjyMHC%2BlyYtDgsnO7i%2BnvfD5pnUK98R11P7UlbP5X3webl78KrvVx5e9%2Fvjc5OTefQh8eSEfh%2B1zRiOje%2B7MwbXxRsnSfdTE4TwLPCcdQs5BzzgY%2BDxNuFBJ4Jn33aUiZE6yRuuStGx21R9Q%2F5Ttym9MzVBQOgz96l9tNyydLY8CpXaV0IDmjB9uJbZyb4VAmcjBw4IpGgXOQD4vav%2B55HjoWaGg4OW5HgfSs7dSm8q6anQKYPNyciBZyPHJwDkHGzHnACAbvd85HifS46x9PonGcWGVv2yxe39Bw%3D%3D"></iframe>


---


# Wiring Guide

## Signal Cables
To build the signal cables, they will look like this
![dupont cables](image/wg_cables_dupont.png)
_Figure: dupont cables_

And also the encoder wires consist of dupont terminals and ribbon cables.
![encoders](image/wg_cable_encoder.png)
_Figure: encoder cables diagram_

## Motors

Here are the cables to power the motors from the motor driver.
![motor leads](image/wg_motor_leads.png)
_Figure: motor leads_

## Motor Driver

The cables to power the motor driver from 12v.
![motor driver](image/wg_motor_driver.png)
_Figure: motor driver wiring_

The motor wires to communicate from CPU to the motor driver.
![motor leads](image/wg_cable_motor_signal.png)
_Figure: motor signal cable_

## Battery
![encoders](image/wg_battery.png)
_Figure: battery components_

## Power

The overview for power cables on SCUTTLE v3
![power overview](image/wg_overview_power.png)
_Figure: power overview_

## Encoders
Encoder wires consist of dupont terminals and ribbon cables.
![encoders](image/wg_cable_encoder.png)
_Figure: encoder cables diagram_


# Wiring Addons
> This section to include popular addons such as RPLIDAR, ultrasonic sensor, and more.

---

# CPU Options
This section covers the differences in wiring for various SBCs (single board computers).

---

## Raspberry PI 4

Overview of wiring SCUTTLE with Pi:
![Pi wiring overview](image/wg_overview_pi.png)
_Figure: Pi wiring overview_

## TI TDA4VM SK "Edge AI"

Overview of wiring SCUTTLE with TDA4VM:
![EDGE AI wiring overview](image/wg_overview_TDA4VM.png)
_Figure: Edge AI wiring overview_


_Edge AI Pinout_
| Function  | PIN |    |  Function |
| --------- | --- | -- | ----- |
| Power_3.3 | 1   | 2  | Power_5.0 |
| I2C_SDA   | 3   | 4  | Power |
| I2C_SCL   | 5   | 6  | GND |
| GPIO      | 7   | 8  | UART_TXD |
| GND       | 9   | 10 | UART_RXD |
| GPIO      | 11  | 12 | I2S_SCLK |
| GPIO      | 13  | 14 | GND |
| GPIO      | 15  | 16 | GPIO |
| Power_3.3 | 17  | 18 | GPIO |
| SPI_MOSI  | 19  | 20 | GND |
| SPI_MISO  | 21  | 22 | GPIO |
| SPI_SCLK  | 23  | 24 | SPI_CS0 |
| GND       | 25  | 26 | SPI_CS1 |
| ID_SDA    | 27  | 28 | ID_SCL |
| GPIO      | 29  | 30 | GND |
| GPIO      | 31  | 32 | PWM0 |
| PWM1      | 33  | 34 | GND |
| I2S_FS    | 35  | 36 | GPIO |
| GPIO      | 37  | 38 | I2S_DIN |
| GND       | 39  | 40 | I2S_DOUT |

---

# 3D Printing

---

> Standard SCUTTLE v3.0 requires about 330g of 3D printed parts.  Everything is designed for manufacturing in FFF with no supports.

![prints overview](image/print_full_set.png)
_Figure: All 3D Printed Parts for a SCUTTLE kit_

# Benchmarking

As an open source community, we aim to gather best practices from leading open projects.  The multidisciplinary nature of SCUTTLE means no existing model fits us, but many elements have been resolved by great communities with an ongoing development and outcomes.

## Community Stars

The organizations in this table have influenced SCUTTLE organization heavily and we continue seeking out best practices from groups like them

| Team              | Site                                                                                          | A Leader in:                                                |
| ----------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Voron 3D Printer  | [Voron Docs](https://docs.vorondesign.com/)                                                   | well-made multidisciplinary documentation                   |
| Thingiverse       | [Thingiverse Library](https://www.thingiverse.com/)                                           | attracted millions - easy to sign up, easy to use           |
| GrabCAD           | [GrabCAD Library](https://grabcad.com/library)                                                | in-browser Visualization - great permalinks - great tagging |
| OpenBuilds        | [openbuilds](https://openbuilds.com/?o=l)                                                     | Attracting high-effort contributions - peak modularity      |
| Leo Rover         | [Leo Dev Resources](https://www.leorover.tech/developers)                                     | Use github for software development                         |
| Printables        | [Printables Library](https://www.printables.com/)                                             | Helps designers post designs with clear licensing           |
| Hackaday          | [Hackaday.io](https://www.hackaday.io/)                                                       | Curating well-engineered designs                            |
| Hackster.io       | [Hackster Contests](https://www.hackster.io/contests)                                         | Attracts all types of designers with nice contests          |
| Leo Rover         | [Leo 3D Models](https://a360.co/378zqRp)                                                      | Convenient in-browser viewing of 3D models                  |
| Viam              | [Viam Discord](https://discord.gg/viam)                                                       | Refined Discord channel for asking questions                |
| Texas Instruments | [TI Robotics Academy](https://dev.ti.com/tirex/global?id=com.ti.Jacinto%20Robotics%20Academy) | Research-grade tasks taught in Edge AI                      |

## Community Thought Leadership

* Linux is the largest open source project in history, and it's founders created [TheOpenSourceWay.org](https://www.theopensourceway.org) to guide other communities.  Their publication called [The Open Source Way](https://www.theopensourceway.org/the_open_source_way-guidebook-2.0.html#_why_do_people_participate_in_open_source_communities) offers insights to how it all works.
* The Open Source Hardware Foundation pushes to engage hardware development teams in open source.  They have regular releases of their [State of Open Source Hardware](https://qr.scuttlerobot.org/g/58a4R641DBp), and this one is from 2021.
* 
