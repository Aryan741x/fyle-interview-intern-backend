-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
WITH TeacherGradingCounts AS (
    SELECT 
        teacher_id, 
        COUNT(id) AS total_graded
    FROM assignments
    WHERE grade IS NOT NULL  -- Only consider graded assignments
    GROUP BY teacher_id
    ORDER BY total_graded DESC
    LIMIT 1
)

SELECT COUNT(*) AS grade_a_count
FROM assignments
WHERE teacher_id = (SELECT teacher_id FROM TeacherGradingCounts)
AND grade = 'A';
