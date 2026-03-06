def display_satellites(overhead_satellites):
    output = []
    intro = "===== Satellites Flying Overhead =====\n\n"
    output.append(intro)
    for cat_name, data in overhead_satellites.items():
        output.append(f"Satellite Category: {cat_name}\n")
        for d in data:
            output.append(f"""
Satellite ID: {d["satid"]}
Satellite Name: {d["satname"]}
Satellite Launch Date: {d["launchDate"]}
Latitude: {d["satlat"]}
Longitude: {d["satlng"]}
Altitude: {d["satalt"]}
\n""")
    return ''.join(output)