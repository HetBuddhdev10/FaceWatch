# FaceWatch
A facial recognition and alerting software


## Inspiration
The inspiration behind FaceWatch was a compelling desire to tackle rising bike thefts in Kingston. We aimed to create a solution that transcended conventional approaches, leveraging facial recognition technology to enhance community safety.

## What it does
FaceWatch is a versatile facial recognition software designed for authorized access. It goes beyond addressing bike thefts, offering a proactive security approach applicable to various scenarios. The system detects faces, granting access exclusively to authorized users, ensuring safety and privacy.

## How we built it
The project began with rigorous research into facial recognition algorithms, utilizing the face_recognition library.  This allowed us to identify faces that would be fed from video cameras and match them with ones that are in the provided database which we hosted in Firebase for this project. The cv2 library was used to capture video and extract faces from it. We prioritized user-friendly interfaces and seamless integration, crafting a robust backend and an intuitive frontend using react. The user side of things shows them location and name of the latest spotting of the face that was recognized which is pulled from the firebase database.

## Challenges we ran into
Challenges primarily revolved around knowledge acquisition and environment setup. Understanding the intricacies of face_recognition and navigating Linux added technical complexities. The shift from a singular bike theft focus to a broader, authorization-based approach required flexibility in implementation. Adapting to these changes, the team overcame challenges, showcasing the resilience and adaptability crucial in a dynamic project environment.

## Accomplishments that we're proud of
Our proudest achievement lies in the seamless functionality of the project's backend. Through meticulous development and rigorous testing, we've successfully created a robust and reliable backbone for FaceWatch. The backend not only meets but exceeds performance expectations, ensuring the smooth operation of the entire system. This accomplishment underscores our commitment to technical excellence and the ability to create a foundation that can support the diverse needs of our users. The user side of the program stands as a testament to our dedication to user experience.

## What we learned
Embarking on the FaceWatch project provided a wealth of learning experiences. Setting up appointments honed organizational skills, and mastering Git improved version control and collaboration. Exploring the face_recognition library enriched technical expertise, and delving into Linux enhanced understanding of system environments. Witnessing idea generation dynamics within the team highlighted the iterative nature of project development.

## What's next for FaceWatch
Mastering Bayun SDK for Enhanced Security
While our achievements with FaceWatch are noteworthy, we acknowledge the need for a deeper understanding of the Bayun SDK to fortify data security further. Addressing this gap is a priority for us, ensuring that the integration of the Bayun SDK is not only complete but also comprehensively understood. This commitment stems from our dedication to upholding the highest standards of data safety and privacy.

Seamless Frontend-Backend Integration
The journey doesn't end with a functional backend and an intuitive user interface; our next immediate step is to establish a seamless connection between the frontend and backend. This integration is pivotal for optimizing user interactions, providing a cohesive experience, and ensuring the efficient flow of information. We are excited about refining this connection to elevate the overall performance and responsiveness of FaceWatch.

Real-world Implementation and User Engagement
Our ultimate goal is to bring FaceWatch to real-life scenarios, making a tangible impact on community safety. 
