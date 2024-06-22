# CArmKinematic
# CArmKinematic

![Demo](demo.mp4)

This repository provides an [online visualizer for C-arm kinematics](https://zyh.science/CArmKinematic). It is based on the prebuilt [mujoco-wasm](https://zalo.github.io/mujoco_wasm/) library. 

C-Arm is commonly used in Digital Subtracted Angiography, as shown in the example image below.
![autocar](navigation_demo.mp4)

The images, or sequence of images, are captured from multiple views, constrained by C-arm kinematics as well as bed translation. This visualizer is used to understand these constraints. In fact, these constraints also provide clues for self-supervised training in reconstruction, as detailed in [AutoCAR](https://autocar.zyh.science).

**Limitations:**

1. Collision detection is disabled mainly for efficiency in the browser, as well as due to the inaccuracy of convex decomposition mesh collision and the fact that SDF collision is only supported in the form of a plug-in in more recent versions of mujoco, e.g. 3.0.
2. It's based on a prebuilt mujoco. If you want to use new features in mujoco or create your own visualizer, please check out the original [mujoco-wasm](https://zalo.github.io/mujoco_wasm/) instead of this, since or building-stage code or resources are removed.

**Related Projects:**

- [AutoCAR](https://autocar.zyh.science): Automatic reconstruction of cardio vessels from sparse views.
- [mujoco-wasm](https://zalo.github.io/mujoco_wasm/): Mujoco 2.3.1 built with emscripten.

This repository provides an [online visualizer for C-arm kinematics](https://zyh.science/CArmKinematic). It is based on the prebuilt [mujoco-wasm](https://zalo.github.io/mujoco_wasm/) library. 

C-Arm is commonly used in Digital Subtracted Angiography, as shown in the example image below.
<!-- include some gif image -->

The images, or sequence of images, are captured from multiple views, constrained by C-arm kinematics as well as bed translation. This visualizer is used to understand these constraints. In fact, these constraints also provide clues for self-supervised training in reconstruction, as detailed in [AutoCAR](https://autocar.zyh.science).

**Limitations:**

1. Collision detection is disabled mainly for efficiency in the browser, as well as due to the inaccuracy of convex decomposition mesh collision and the fact that SDF collision is only supported in the form of a plug-in in more recent versions of mujoco, e.g. 3.0.
2. It's based on a prebuilt mujoco. If you want to use new features in mujoco or create your own visualizer, please check out the original [mujoco-wasm](https://zalo.github.io/mujoco_wasm/) instead of this, since or building-stage code or resources are removed.

**Related Projects:**

- [AutoCAR](https://autocar.zyh.science): Automatic reconstruction of cardio vessels from sparse views.
- [mujoco-wasm](https://zalo.github.io/mujoco_wasm/): Mujoco 2.3.1 built with emscripten.

