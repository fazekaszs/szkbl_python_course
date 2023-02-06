# Declare necessary constants
speed_of_light = 1.07925285E9
mph_to_kmh = 1.60934

# Query the user for the input data
horse_velocity = float(input("Velocity of the horse (in mph): "))
arrow_velocity = float(input("Velocity of the arrow (in mph): "))

# Convert from miles/h to km/h
horse_velocity *= mph_to_kmh
arrow_velocity *= mph_to_kmh

# Simple velocity addition
observed_arrow_velocity = horse_velocity + arrow_velocity

print("The observed velocity without corrections in km/h:", observed_arrow_velocity)

# Do the relativistic corrections
observed_arrow_velocity = horse_velocity * arrow_velocity
observed_arrow_velocity /= speed_of_light ** 2
observed_arrow_velocity += 1
observed_arrow_velocity = (horse_velocity + arrow_velocity) / observed_arrow_velocity

print("The observed velocity with corrections in km/h:", observed_arrow_velocity)
