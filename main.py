def study_planner():
    print("=" * 50)
    print("             STUDY PLANNER")
    print("=" * 50)
    name = input("Enter your name: ")
    subject = input("Enter your subject: ")
    hours = float(input("How many hours can you study? "))
    level = input("Enter level (Beginner/Intermediate/Advanced): ")
    print("\n----- STUDY SUMMARY -----")
    print("Student :", name)
    print("Subject :", subject)
    print("Time    :", hours, "hours")
    print("Level   :", level)
    minutes = int(hours * 60)
    sessions = minutes // 30
    if level.lower() == "beginner":
        focus, activity = "Learn basic concepts.", "Read theory and solve easy questions."
    elif level.lower() == "intermediate":
        focus, activity = "Understand concepts and practice.", "Revise theory and solve mixed questions."
    else:
        focus, activity = "Improve difficult concepts.", "Solve advanced questions and tests."
    study = sessions * 25
    print("\n----- PERSONALIZED PLAN -----")
    print("Phase 1: Concept Learning")
    print("Duration:", study // 3, "minutes")
    print("Goal:", focus)
    print("\nPhase 2: Practice")
    print("Duration:", study // 3, "minutes")
    print("Activity:", activity)
    print("\nPhase 3: Revision")
    print("Duration:", study - 2 * (study // 3), "minutes")
    print("Activity: Review your notes.")
    print("\nPhase 4: Self Test")
    print("Duration: 15 minutes")
    print("Activity: Take a short quiz.")
    print("\n----- TIME PLAN -----")
    for i in range(1, sessions + 1):
        print("Session", i, ": 25 min Study | 5 min Break")
    print("\nRemember: Study -> Practice -> Revise -> Test")
    print("Stay consistent!")

study_planner()

