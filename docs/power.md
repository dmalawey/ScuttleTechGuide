# Power Budget
> A dedicated section for budgeting power. This contains details the power system onboard SCUTTLE.  With extensibility as a central goal for SCUTTLE, we aim to offer sufficient detail to let you engineer any new function or actuator you can dream of.

This chart indicates the power loads of each component on your power supply.

![pwr_loads_chart](/image/pwr_chart_loads.png ':class=image-25')

This table describes the estimated duty cycles for key components in a typical operating scenario.

![Chart of Duty Cycles](/image/pwr_table_dutyCycles.png ':class=image-30')

The raspberry pi and any loads that source power from it, ultimately source power from the 5v DC adapter.  This adapter has an efficiency curve as shown.  Note that the adapter has a constant power draw when the 12v source (battery) is powered on and hooked up.

![DC adapter efficiency chart](/image/pwr_dc5v_efficiency.png ':class=image-25')

---

## DIN Power

Quick guide steps to route power with DIN rail.

1. Use a simple DIN bracket to secure a terminal.  Drill out the center hole to 4mm.
2. Use an M2.5x12mm screw and M2.5 heat-set insert.
3. If you have a deburring tool, deburr your hole for a cleaner insertion.
4. Insert the thead to a flush position.
5. use a zip tie to secure the cable.
6. We recommend the terminal pair for the power source is secured and the load pair is free.
7. secure your source wires into the power distribution terminals and the DIN bracket onto your rail.
Now your power source is ready for quick plugging!

### Images

Images for general power distribution components & examples.

![drill bit](https://i.imgur.com/D3sDUlU.jpg)

![fasteners](https://i.imgur.com/UkaOBIx.jpg)

![deburring tool](https://i.imgur.com/CLA0Gfc.jpg)

![threads inserted](https://i.imgur.com/iEK601h.jpg)

![zip tie positioning](https://i.imgur.com/kiJwb7D.jpg)

![source and load](https://i.imgur.com/lM1F4Kr.jpg)

![power rail and source terminal](https://i.imgur.com/quijDQi.jpg)
