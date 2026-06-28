{ config, pkgs, ... }:

{
  #################################################
  ## Imports
  #################################################

  imports = [
    ./hardware-configuration.nix
  ];

  #################################################
  ## Boot
  #################################################

  boot.loader.systemd-boot.enable = true;
  boot.loader.systemd-boot.configurationLimit = 5;
  boot.loader.efi.canTouchEfiVariables = true;
  boot.loader.timeout = 0;

  boot.kernelPackages = pkgs.linuxPackages_latest;

  boot.consoleLogLevel = 3;
  boot.initrd.verbose = false;

  boot.kernelParams = [
    "quiet"
    "splash"
  ];

  boot.plymouth.enable = true;

  #################################################
  ## Networking
  #################################################

  networking.hostName = "nixos";
  networking.networkmanager.enable = true;
  networking.firewall.enable = true;

  #################################################
  ## Time & Locale
  #################################################

  time.timeZone = "Asia/Kolkata";

  i18n.defaultLocale = "en_IN";

  i18n.extraLocaleSettings = {
    LC_ADDRESS = "en_IN";
    LC_IDENTIFICATION = "en_IN";
    LC_MEASUREMENT = "en_IN";
    LC_MONETARY = "en_IN";
    LC_NAME = "en_IN";
    LC_NUMERIC = "en_IN";
    LC_PAPER = "en_IN";
    LC_TELEPHONE = "en_IN";
    LC_TIME = "en_IN";
  };

  #################################################
  ## Desktop
  #################################################

  services.xserver.enable = true;

  services.xserver.displayManager.lightdm.enable = true;
  services.desktopManager.pantheon.enable = true;

  services.xserver.xkb = {
    layout = "us";
    variant = "";
  };

  #################################################
  ## Audio
  #################################################

  services.pulseaudio.enable = false;

  security.rtkit.enable = true;

  services.pipewire = {
    enable = true;

    alsa.enable = true;
    alsa.support32Bit = true;

    pulse.enable = true;

    # jack.enable = true;
  };

  #################################################
  ## Power Management
  #################################################

  powerManagement.cpuFreqGovernor = "schedutil";

  #################################################
  ## Services
  #################################################

  services.usbmuxd.enable = true;
  services.printing.enable = true;

  services.fstrim.enable = true;
  services.fwupd.enable = true;
  services.power-profiles-daemon.enable = true;
  services.timesyncd.enable = true;

  #################################################
  ## Users
  #################################################

  users.users.farhan = {
    isNormalUser = true;
    description = "Farhan";

    extraGroups = [
      "wheel"
      "networkmanager"
    ];
  };

  #################################################
  ## Programs
  #################################################

  programs.firefox.enable = false;

  #################################################
  ## Nix
  #################################################

  nixpkgs.config.allowUnfree = true;

  nix = {

    settings = {
      experimental-features = [
        "nix-command"
        "flakes"
      ];

      auto-optimise-store = true;
    };

    gc = {
      automatic = true;
      dates = "weekly";
      options = "--delete-older-than 30d";
    };

    optimise.automatic = true;
  };

  #################################################
  ## Packages
  #################################################

  environment.systemPackages = with pkgs; [

    ######## Browsers ########

    google-chrome
    mullvad-browser

    ######## Development ########

    git
    vscode
    python3
    gcc
    gnumake
    cmake

    ######## Editors ########

    kdePackages.kate

    ######## Terminal ########

    wget
    curl
    tree
    htop
    btop
    fastfetch

    ripgrep
    fd
    file
    jq

    pciutils
    usbutils
    lsof
    ncdu

    unzip
    zip
    p7zip

    ######## Media ########

    mpv
    easyeffects

    ######## Downloads ########

    aria2
    persepolis
    yt-dlp

    ######## Apple ########

    ifuse
    libimobiledevice
    usbmuxd

    ######## Utilities ########

    pwvucontrol
    crosspipe

    ######## Office ########

    onlyoffice-desktopeditors
  ];

  #################################################
  ## System
  #################################################

  system.stateVersion = "26.05";
}