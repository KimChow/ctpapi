import platform

from setuptools import Extension, setup

dir_path = "ctpapi"
runtime_library_dirs = []
if platform.uname().system == "Windows":
    compiler_flags = [
        "/MP", "/std:c++17",  # standard
        "/O2", "/Ob2", "/Oi", "/Ot", "/Oy", "/GL",  # Optimization
        "/wd4819"  # 936 code page
    ]
    extra_link_args = []

else:
    compiler_flags = [
        "-std=c++17",  # standard
        "-O3",  # Optimization
        "-Wno-delete-incomplete", "-Wno-sign-compare", "-pthread"
    ]
    extra_link_args = ["-lstdc++"]
    runtime_library_dirs = ["$ORIGIN"]

vnctpmd = Extension(
    # 指定 vnctpmd 的位置
    "ctpapi.ctp.vnctpmd",
    [
        f"{dir_path}/ctp/vnctp/vnctpmd/vnctpmd.cpp",
    ],
    # 编译需要的头文件
    include_dirs=[
        f"{dir_path}/ctp/include",
        f"{dir_path}/ctp/vnctp",
    ],
    # 指定为c plus plus
    language="cpp",
    define_macros=[],
    undef_macros=[],
    # 依赖目录
    library_dirs=[f"{dir_path}/ctp/libs", f"{dir_path}/ctp"],
    # 依赖项
    libraries=["thostmduserapi_se", "thosttraderapi_se", ],
    extra_compile_args=compiler_flags,
    extra_link_args=extra_link_args,
    depends=[],
    runtime_library_dirs=runtime_library_dirs,
)
vnctptd = Extension(
    "ctpapi.ctp.vnctptd",
    [
        f"{dir_path}/ctp/vnctp/vnctptd/vnctptd.cpp",
    ],
    include_dirs=[
        f"{dir_path}/ctp/include",
        f"{dir_path}/ctp/vnctp",
    ],
    define_macros=[],
    undef_macros=[],
    library_dirs=[f"{dir_path}/ctp/libs", f"{dir_path}/ctp"],
    libraries=["thostmduserapi_se", "thosttraderapi_se"],
    extra_compile_args=compiler_flags,
    extra_link_args=extra_link_args,
    runtime_library_dirs=runtime_library_dirs,
    depends=[],
    language="cpp",
)

if platform.system() == "Windows":
    # use pre-built pyd for windows ( support python 3.7 only )
    ext_modules = [vnctptd, vnctpmd]
elif platform.system() == "Darwin":
    ext_modules = []
else:
    ext_modules = [vnctptd, vnctpmd]

pkgs = ['ctpapi', 'ctpapi.ctp']
install_requires = []
setup(
    name='ctpapi',
    version='1.0',
    description="good luck",
    author='somewheve',
    author_email='####',
    license="MIT",
    packages=pkgs,
    install_requires=install_requires,
    platforms=["Windows", "Linux", "Mac OS-X"],
    package_dir={'ctpapi': 'ctpapi/'},
    package_data={'ctpapi': ['ctp/*', ]},
    ext_modules=ext_modules,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ]
)
