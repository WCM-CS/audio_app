package main

import (
	"fmt"
	"net/http"
)

// Function to ping API via get request
func keepAlive() (*http.Response, error) {
	// Call my audio API hosted on render
	resp, err := http.Get("https://audio-app-api.onrender.com/api/audio-files")
	if err != nil {
		// Returns error
		return nil, fmt.Errorf("error fetching API: %v", err)
	}
	// Returns ok
	return resp, nil
}

func main() {
	// Call API request
	res, err := keepAlive()
	if err != nil {
		fmt.Println("Failed to keep alive:", err)
		return
	}
	// Ensure body is closed
	defer res.Body.Close()
	// Return response status
	fmt.Println("Get http command, response status:", res.Status)
}
