import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { DataService } from './data.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'frontend';

  constructor(private dataService: DataService) {}

  generateImage(): void {
    this.dataService.refreshImage().subscribe(
      () => {
        // Success callback, you can update UI here if needed
        console.log('Image generated successfully');
      },
      error => {
        // Error callback, handle error appropriately
        console.error('Error generating image:', error);
      }
    );
  }
}
