# OpenVerne

rocket (or missile) Instantaneous Impact Point(IIP) calculation

The instantaneous impact point (IIP) of a rocket, given its position and velocity,
is defined as its touchdown point(altitude=0[m]) assuming a free-fall flight (without propulsion).
The IIP is considered as a very important information for safe launch operation of a rocket.

ロケットの瞬間落下地点（IIP : Instantaneous Impact Point)を計算できるスクリプト
緯度[deg]経度[deg]高度[m]と北方向速度[m/s]東方向速度[m/s]鉛直下方向速度[m/s]を入力すると
IIPの座標が出力される。

## Usage
see example(example_xx.py in this repository).

## Coordinate
Regarding the position, it must be inputted at latitude and longitude altitude.(LLH)

For speed, input it in the North, East and Down direction coordinate system at that latitude, longitude and altitude.(NED)

## IIP class constractor

```python
IIP(np.array([latitude, longitude, altitude]), np.array([North, East, Down]))
```

The first argument is the position in the LLH coordinate system [deg, deg, m]

The second argument is the speed in the NED coordinate system [m/s, m/s, m/s]

## Refarence
Jaemyung Ahn and Woong-Rae Roh.  "Noniterative Instantaneous Impact Point Prediction Algorithm for Launch Operations",
Journal of Guidance, Control, and Dynamics, Vol. 35, No. 2 (2012), pp. 645-648.
https://doi.org/10.2514/1.56395

Young-Woo Nam, Taehyun Seong, and Jaemyung Ahn.  "Adjusted Instantaneous Impact Point and New Flight Safety Decision Rule", Journal of Spacecraft and Rockets, Vol. 53, No. 4 (2016), pp. 766-773.
https://doi.org/10.2514/1.A33424

## Conception of name
[Jules Verne](https://en.wikipedia.org/wiki/Jules_Verne) ([From_the_Earth_to_the_Moon](https://en.wikipedia.org/wiki/From_the_Earth_to_the_Moon))




## License
OpenVerne is an Open Source project licensed under the MIT License
