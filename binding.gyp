{
  "targets": [
    {
      "target_name": "forcefocus",
      "sources": [
        "src/bindings.cc"
      ],
      "cflags": [
        "-Wall",
        "-Wparentheses",
        "-Winline",
        "-Wbad-function-cast",
        "-Wdisabled-optimization",
        "-std=c++17"
      ],
      "cflags_cc": [
        "-std=c++17"
      ],
      "conditions": [
        [
          "OS==\"win\"",
          {
            "sources": ["src/forcefocus_win.cc"],
            "msvs_settings": {
              "VCCLCompilerTool": { "ExceptionHandling": 1, "AdditionalOptions": [ "-std:c++17" ] }
            }
          }
        ],
        [
          "OS!=\"win\"",
          {
            "sources": ["src/forcefocus_noop.cc"]
          }
        ]
      ]
    }
  ]
}
