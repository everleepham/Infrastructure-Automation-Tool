def generate_script(config: dict) -> str:
    script = f"hostname {config.get('hostname', '')}\n"
    for iface in config.get("interfaces", []):
        script += f"interface {iface['name']}\n"
        script += f" ip address {iface['ip']} {iface['mask']}\n"
        script += " no shutdown\n"
    return script
