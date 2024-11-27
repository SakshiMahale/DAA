#include <iostream>
#include <string>
#include <iomanip> // for controlling floating point precision
using namespace std;

// Function to convert grade to numeric value
int convertGrade(const string &grade)
{
    if (grade == "AA")
        return 10;
    if (grade == "AB")
        return 9;
    if (grade == "BB")
        return 8;
    if (grade == "BC")
        return 7;
    if (grade == "CC")
        return 6;
    if (grade == "CD")
        return 5;
    if (grade == "DD")
        return 4;
    if (grade == "FF")
        return 0;
    return -1; // Invalid grade
}

// Function to calculate SPI for one semester
float calculateSPI()
{
    int numSubjects;
    cout << "Enter the number of subjects: ";
    cin >> numSubjects;

    int totalCredits = 0, totalPoints = 0;

    for (int i = 0; i < numSubjects; i++)
    {
        int credits;
        string grade;
        cout << "Enter credits and grade for subject " << i + 1 << ": ";
        cin >> credits >> grade;

        int numericGrade = convertGrade(grade);
        if (numericGrade == -1)
        {
            cout << "Invalid grade! Please enter valid grades (AA, AB, BB, etc.).\n";
            i--; // Repeat for this subject
        }
        else
        {
            totalCredits += credits;
            totalPoints += credits * numericGrade;
        }
    }

    if (totalCredits == 0)
    {
        cout << "Total credits cannot be zero. SPI calculation failed.\n";
        return -1;
    }

    float spi = static_cast<float>(totalPoints) / totalCredits;
    cout << "SPI for the semester: " << fixed << setprecision(2) << spi << endl;
    return spi;
}

// Function to calculate CPI over multiple semesters
void calculateCPI()
{
    int numSemesters;
    cout << "Enter the number of semesters: ";
    cin >> numSemesters;

    if (numSemesters <= 0)
    {
        cout << "Invalid number of semesters!\n";
        return;
    }

    float totalSPI = 0;

    for (int i = 0; i < numSemesters; i++)
    {
        cout << "Calculating SPI for Semester " << i + 1 << ":\n";
        float spi = calculateSPI();
        if (spi == -1)
        {
            cout << "Error in SPI calculation. CPI cannot be calculated.\n";
            return;
        }
        totalSPI += spi;
    }

    float cpi = totalSPI / numSemesters;
    cout << "Final CPI after " << numSemesters << " semesters: " << fixed << setprecision(2) << cpi << endl;
}

// Main function to choose between SPI and CPI
int main()
{
    int choice;
    cout << "Choose an option:\n1. Calculate SPI\n2. Calculate CPI\n";
    cin >> choice;

    if (choice == 1)
    {
        calculateSPI();
    }
    else if (choice == 2)
    {
        calculateCPI();
    }
    else
    {
        cout << "Invalid option!\n";
    }
    return 0;
}
