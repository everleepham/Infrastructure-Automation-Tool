


def generate_script(config: dict) -> str:
    interface = ''
    script = ''
    for key, value in config.items():
        if key == "hostname":
            script += f"hostname {value}\n"
        elif key == "interfaces":
            for value in config[key]:
                interface += f"interface {value['name']}\n"
                interface += f" ip address {value['ip']} {value['mask']}\n"
                interface += " no shutdown\n"
            script += interface
    return script


config = {
    "hostname": "R1",
    "interfaces": [
        {"name": "Gig1", "ip": "10.0.0.1", "mask": "255.255.255.0"}
    ]
}

print(generate_script(config))