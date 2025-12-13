{
  description = "Python development shells with Nix";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
  }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = import nixpkgs {inherit system;};
      pythonRepo = pkgs.python313Packages;
    in {
      devShells.default = pkgs.mkShell {
          packages = [
            pkgs.uv
            pkgs.python313
          ];

          LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
            pkgs.stdenv.cc.cc
            pkgs.zlib
            pkgs.glib
            pkgs.libGL
          ];

          UV_PYTHON = "${pkgs.python313}/bin/python3";
        };
    });
}
