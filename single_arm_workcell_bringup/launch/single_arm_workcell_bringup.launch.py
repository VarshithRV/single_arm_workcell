from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():
    ur_type_arg = DeclareLaunchArgument(
        "ur_type",
        default_value="ur16e",
        description="Type of UR robot (e.g., ur16e)"
    )

    robot_ip_arg = DeclareLaunchArgument(
        "robot_ip",
        default_value="localhost",
        description="IP address of the robot"
    )

    use_fake_hw_arg = DeclareLaunchArgument(
        "use_fake_hardware",
        default_value="false",
        description="Use fake hardware (true/false)"
    )


    ur_type = LaunchConfiguration("ur_type")
    robot_ip = LaunchConfiguration("robot_ip")
    use_fake_hardware = LaunchConfiguration("use_fake_hardware")

    driver_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                FindPackageShare("single_arm_workcell_driver"),
                "launch",
                "single_arm_workcell_control.launch.py"
            ])
        ),
        launch_arguments={
            "ur_type": ur_type,
            "robot_ip": robot_ip,
            "use_fake_hardware": use_fake_hardware,
        }.items()
    )
    moveit_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                FindPackageShare("single_arm_workcell_moveit_config"),
                "launch",
                "single_arm_workcell_moveit.launch.py"
            ])
        ),
        launch_arguments={
            "ur_type": ur_type,
        }.items()
    )

    return LaunchDescription([
        ur_type_arg,
        robot_ip_arg,
        use_fake_hw_arg,
        driver_launch,
        moveit_launch,
    ])