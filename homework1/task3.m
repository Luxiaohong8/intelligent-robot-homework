path = [2.00 1.00;1.25 1.75;5.25 7.75;7.25 12.25;11.75 7.25;11.00 9.00];

R_current_location=path(1,:);
R_goal_location=path(end,:);
initialOrientation = 0;
R_current_pos=[R_current_location initialOrientation];
R_radius=0.4;

plot(path(:,1), path(:,2),'k--d')
xlim([0 13])
ylim([0 13])

robot = ExampleHelperDifferentialDriveRobot(R_current_pos);

controller=robotics.PurePursuit;
controller.Waypoints = path;
controller.DesiredLinearVelocity = 0.3;
controller.MaxAngularVelocity = 2;
controller.LookaheadDistance = 0.5;
goalRadius = 0.1;

distanceToGoal = norm(R_current_location - robotGoal);

while( distanceToGoal > goalRadius )

    % Compute the controller outputs, i.e., the inputs to the robot
    [v, omega] = step(controller, robot.CurrentPose);

    % Simulate the robot using the controller outputs.
    drive(robot, v, omega)

    % Extract current location information ([X,Y]) from the current pose of the
    % robot
    R_current_location = robot.CurrentPose(1:2);

    % Re-compute the distance to the goal
    distanceToGoal = norm(R_current_location - robotGoal);
end