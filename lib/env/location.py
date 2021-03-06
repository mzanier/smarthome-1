
# lib/env/location.py

if sh.sun:
    try:
        sunrise = sh.sun.rise().astimezone(sh.tzinfo())
        sh.env.location.sunrise(sunrise)
    except Exception as e:
        logger.error("ephem error while calculating sun rise: {}".format(e))
        
    azimut_rise_radians, elevation_rise_radians = sh.sun.pos(dt=sunrise)
    azimut_rise_degrees, elevation_rise_degrees = sh.sun.pos(dt=sunrise, degree=True)
    sh.env.location.sunrise.azimut.degrees(round(azimut_rise_degrees, 2))
    sh.env.location.sunrise.elevation.degrees(round(elevation_rise_degrees, 2))
    sh.env.location.sunrise.azimut.radians(round(azimut_rise_radians,2))
    sh.env.location.sunrise.elevation.radians(round(elevation_rise_radians,2))

    try:
        sunset = sh.sun.set().astimezone(sh.tzinfo())
        sh.env.location.sunset(sunset)
    except Exception as e:
        logger.error("ephem error while calculating sun set: {}".format(e))

    azimut_set_radians, elevation_set_radians = sh.sun.pos(dt=sunset)
    azimut_set_degrees, elevation_set_degrees = sh.sun.pos(dt=sunset, degree=True)
    sh.env.location.sunset.azimut.degrees(round(azimut_set_degrees, 2))
    sh.env.location.sunset.elevation.degrees(round(elevation_set_degrees, 2))
    sh.env.location.sunset.azimut.radians(round(azimut_set_radians,2))
    sh.env.location.sunset.elevation.radians(round(elevation_set_radians,2))

    # setting altitude/azimut
    azimut, elevation = sh.sun.pos()

    time = datetime.datetime.utcnow()
    azimut_radians, elevation_radians = sh.sun.pos(dt=time)
    azimut_degrees, elevation_degrees = sh.sun.pos(dt=time, degree=True)
    sh.env.location.sun_position.azimut.degrees(round(azimut_degrees, 2))
    sh.env.location.sun_position.elevation.degrees(round(elevation_degrees, 2))
    sh.env.location.sun_position.azimut.radians(round(azimut_radians,2))
    sh.env.location.sun_position.elevation.radians(round(elevation_radians,2))

    try:
        sh.env.location.moonrise(sh.moon.rise().astimezone(sh.tzinfo()))
    except Exception as e:
        logger.error("ephem error while calculating moon rise: {}".format(e))
    try:
        sh.env.location.moonset(sh.moon.set().astimezone(sh.tzinfo()))
    except Exception as e:
        logger.error("ephem error while calculating moon set: {}".format(e))

    sh.env.location.moonphase(sh.moon.phase())

    # setting day and night
    try:
        day = sh.sun.rise(-6).day != sh.sun.set(-6).day
        sh.env.location.day(day)
        sh.env.location.night(not day)
    except Exception as e:
        logger.error("ephem error while calculating day/night: {}".format(e))
